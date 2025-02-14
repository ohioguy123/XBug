document.addEventListener('DOMContentLoaded', function() {
  chrome.storage.local.get('jsRequests', function(result) {
    const jsRequests = result.jsRequests || [];
    const list = document.getElementById('js-requests-list');
    jsRequests.forEach(url => {
      const listItem = document.createElement('li');
      listItem.textContent = url;
      list.appendChild(listItem);
    });
  });
});

