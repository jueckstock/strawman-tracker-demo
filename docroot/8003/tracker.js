(function() {
    const identifier = (() => {
        const trackerSymbol = '8003.tracker.identifier';
        let storedIdentifier = localStorage.getItem(trackerSymbol)
        if (!storedIdentifier) {
            const url = new URL(window.location.href)
            if (url.searchParams.has("t8id")) {
                storedIdentifier = url.searchParams.get("t8id")
            } else {
                const array = new Uint8Array(16);
                window.crypto.getRandomValues(array);
                storedIdentifier = array.reduce((a, b) => a + b.toString(16))
            }
            localStorage.setItem(trackerSymbol, storedIdentifier)
        }
        return storedIdentifier
    })();
    console.log(`TRACKER: you are #${identifier}`)

    window.addEventListener('load', () => {
        document.querySelectorAll("a[href]").forEach(el => {
            const oldUrl = new URL(el.getAttribute("href"))
            oldUrl.searchParams.set("t8id", identifier)
            el.setAttribute("href", oldUrl.toString())
        })
    });
})();