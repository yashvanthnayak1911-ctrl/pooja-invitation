document.addEventListener('DOMContentLoaded', () => {
    const book = document.getElementById('book');
    const spiralsContainer = document.getElementById('spirals');

    // Create 11 spirals for the binding
    const numSpirals = 11;
    for (let i = 0; i < numSpirals; i++) {
        const spiral = document.createElement('div');
        spiral.className = 'spiral';
        spiralsContainer.appendChild(spiral);
    }

    // Add corresponding holes to each page
    const addHoles = (pageContent) => {
        const isBack = pageContent.closest('.back');
        const ringContainer = document.createElement('div');
        ringContainer.className = 'holes-container';

        if (isBack) {
            ringContainer.classList.add('holes-right');
        }

        for (let i = 0; i < numSpirals; i++) {
            const hole = document.createElement('div');
            hole.className = 'hole';
            ringContainer.appendChild(hole);
        }
        pageContent.prepend(ringContainer);
    };

    document.querySelectorAll('.content').forEach(addHoles);

    let currentZ = 10;
    let flippedPages = 0;

    window.flipNext = function (pageId) {
        const page = document.getElementById(pageId);
        if (!page) return;

        page.style.zIndex = currentZ++;
        page.classList.add('flipped');
        flippedPages++;

        if (flippedPages > 0) {
            book.classList.add('open');
        }
    };

    window.flipBack = function (pageId) {
        const page = document.getElementById(pageId);
        if (!page) return;

        page.classList.remove('flipped');
        flippedPages--;

        if (flippedPages === 0) {
            book.classList.remove('open');
        }

        // Restore original z-index after transition completes
        setTimeout(() => {
            page.style.zIndex = page.dataset.z;
        }, 1200);
    };
});
