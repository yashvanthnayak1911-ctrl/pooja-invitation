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

    // Generate random background flowers
    const bgContainer = document.getElementById('bg-flowers');
    if (bgContainer) {
        const flowerTypes = ['✿', '❀', '❁'];
        const numFlowers = 40; // The "some number" of small white flowers

        for (let i = 0; i < numFlowers; i++) {
            const flower = document.createElement('div');
            flower.className = 'flower';

            // Randomly select emoji
            flower.textContent = flowerTypes[Math.floor(Math.random() * flowerTypes.length)];

            // Randomize position (0% to 100% of viewport)
            const posX = Math.random() * 100;
            const posY = Math.random() * 100;

            // Randomize size (small to medium, 15px to 45px)
            const size = Math.random() * 30 + 15;

            // Randomize rotation speed and direction
            const spinDuration = Math.random() * 60 + 40; // 40s to 100s for a slow peaceful drift
            const spinDirection = Math.random() > 0.5 ? 'float-spin-1' : 'float-spin-2';

            // Randomize starting animation delay so they don't all move in sync
            const delay = Math.random() * -100;

            // Apply styles
            flower.style.left = `${posX}vw`;
            flower.style.top = `${posY}vh`;
            flower.style.fontSize = `${size}px`;
            flower.style.animation = `${spinDirection} ${spinDuration}s linear infinite`;
            flower.style.animationDelay = `${delay}s`;

            // Subtle random opacity for depth
            flower.style.opacity = (Math.random() * 0.15 + 0.1).toFixed(2);

            bgContainer.appendChild(flower);
        }
    }
});
