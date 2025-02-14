(function() {
  // Get the URL of the script to be injected
  const scriptSrc = chrome.runtime.getURL('lazyegg-injected.js');                                                                                                                  
  
  // Create a script tag and set its src attribute
  const scriptTag = document.createElement('script');
  scriptTag.src = scriptSrc;

  // Ensure the script is executed immediately and removed afterward
  scriptTag.onload = function() {
    this.remove();
  };

  // Insert the script tag at the very beginning of the head or document
  const headOrHtml = document.head || document.documentElement;
  headOrHtml.insertBefore(scriptTag, headOrHtml.firstChild);
})();

(function() {
  const chest_local = {};

  const key = 'jsRequests';
  const value = localStorage.getItem(key);
  if (value) {
    console.log(`${key}: ${value}`);
    chest_local[key] = value;
  }

  chrome.storage.local.set({ chest_local }, function() {
    console.log('localStorage.jsRequests copied to chest_local', chest_local);
  });
})();

