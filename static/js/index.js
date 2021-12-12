$("#search-movies-btn").click(function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $(".search-form-container").offset().top
    }, 1400);
});

function showResults() {
    const content = document.getElementByClassName('content');
    const searchResults = document.getElementByClassName('search-results');
    const clone = searchResults.cloneNode(true);

    content.replaceWith(clone);
}

