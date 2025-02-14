chrome.storage.local.get('chest_local', function(result) {
	const jsRequests = JSON.parse(result.chest_local.jsRequests);
	const urls = jsRequests.map(url => new URL(url).href);
	  console.log(urls);
});
