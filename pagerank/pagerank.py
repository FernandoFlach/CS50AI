import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print("corpus", corpus)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    page_links = corpus[page]
    new_dict = {}

    if len(page_links) > 0:
        GENERAL_PROBABILITY = (1 - damping_factor) / len(corpus.keys())
        LINKED_PAGE_PROBABILITY = (damping_factor / len(page_links)) + GENERAL_PROBABILITY

        for i in page_links:
                new_dict[i] = LINKED_PAGE_PROBABILITY

        # Probability for every page in the corpus (1 - damping factor)
        for i in corpus:
            if not new_dict.get(i, 0):
                new_dict[i] = GENERAL_PROBABILITY

        return new_dict
    
    else:
        # If the page has no links
        probability = 1 / len(corpus.keys())
        for i in corpus.keys():
            new_dict[i] = probability

        return new_dict

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # pegar o transition model e escolher uma pagina, ai fazer o transition model dessa pagina
    new_dict = {}
    for key in corpus:
        new_dict[key] = 0

    
    selected_page = random.choice(list(corpus.keys())) # FIRST PAGE
    new_dict[selected_page] = 1
    
    for i in range(n-1):
        probabilities = transition_model(corpus, selected_page, damping_factor)
        sorted_dict = dict(sorted(probabilities.items()))
        selected_page = random.choices(list(corpus.keys()), weights=sorted_dict.values())[0]
        new_dict[selected_page] += 1
        
    for item in new_dict:
        new_dict[item] /= n

    return new_dict

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    N = len(corpus) # Number of pages in corpus
    pageranks = {}
    updated_pageranks = {}

    initial_pagerank = 1 / N # INITIAL PAGERANK
    for i in corpus:
        pageranks[i] = initial_pagerank

    loop = True
    while loop:
        for p in corpus:  # To iterate over every p in corpus and calculate its pageranl

            # Probability for random page divided by the number of pages
            conditional1 = (1 - damping_factor) / N 
            conditional2_total = 0
            
            for i in corpus: # for every i page in corpus, to check its links
                
                # If i has no links, consider that it has one for each page including itself
                if len(corpus[i]) == 0: 
                    conditional2_total += pageranks[i] * initial_pagerank   

                elif p in corpus[i]:
                    # I's pagerank divided by its number of links
                    conditional2 = pageranks[i] / len(corpus[i])

                    conditional2_total += conditional2

            new_pagerank = conditional1 + (damping_factor * conditional2_total)
            updated_pageranks[p] = new_pagerank

        if abs(pageranks[p] - new_pagerank) < 0.001:
            loop = False
        pageranks = updated_pageranks.copy()
        
    return pageranks


if __name__ == "__main__":
    main()
