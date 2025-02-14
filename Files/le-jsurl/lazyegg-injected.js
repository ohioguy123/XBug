(function() {
  console.log("lazyegg");
  // Hook into the network request events
  const lazyeggObserver = new PerformanceObserver((list) => {
    list.getEntries().forEach((entry) => {
      try {
        const xero = entry.name.split(/[?#]/)[0];
        if (xero.match(/\.js([?#]|)$/)) {
          console.log('JavaScript request:', xero);
          // Retrieve current data from localStorage
          let jsRequests = JSON.parse(localStorage.getItem('jsRequests')) || [];
          
          // Check if the request already exists
          if (!jsRequests.includes(xero)) {
            jsRequests.push(xero);
            // Save updated data back to localStorage
            localStorage.setItem('jsRequests', JSON.stringify(jsRequests));
          }
        }
      } catch (error) {
        console.error('Error processing entry:', error);
      }
    });
  });

  // Start observing network requests
  lazyeggObserver.observe({ entryTypes: ['resource'] });
})();

