self.addEventListener('install', function(event) {
  console.log('Service worker installed');
});

// Activate service worker
self.addEventListener('activate', function(event) {
  console.log('Service worker activated');
});

// Listen for fetch events
self.addEventListener('fetch', function(event) {
  console.log('Fetch event:', event.request.url);
  // You can add your custom logic for handling fetch requests here
});

// Listen for message events from client
self.addEventListener('message', function(event) {
  console.log('Message event:', event.data);
  // You can add your custom logic for handling messages from client here
});

// Retrieve data from chrome storage
chrome.storage.local.get('chest_local', function(result) {
  const jsRequests = JSON.parse(result.chest_local.jsRequests);
  const treasureElement = document.getElementById('treasure');

  // Loop through each URL and create a new element for each
  jsRequests.forEach(url => {
    const line = document.createElement('div');
    line.textContent = url;
    applyStyles(line, 'chest_local');
    treasureElement.appendChild(line);
  });

  // Create and append the download button
  const downloadButton = document.createElement('button');
  downloadButton.textContent = 'Download URLs';
  downloadButton.addEventListener('click', () => downloadUrls(jsRequests));
  treasureElement.appendChild(downloadButton);
});

function applyStyles(element, key) {
  if (key === 'chest_local') {
    element.style.display = 'inline-white';
    element.style.backgroundColor = 'white';
    element.style.color = 'black';
    element.style.fontWeight = 'bold';
    element.style.padding = '3px 7px 3px 7px';
    element.style.borderRadius = '3px';
  } else {
    element.style.display = 'inline-block';
    element.style.backgroundColor = 'black';
    element.style.color = 'white';
    element.style.fontWeight = 'bold';
    element.style.padding = '3px 7px 3px 7px';
    element.style.borderRadius = '3px';
  }
}

function downloadUrls(urls) {
  const blob = new Blob([urls.join('\n')], { type: 'text/plain' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'jsurls.txt';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

