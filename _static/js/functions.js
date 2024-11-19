function findRelativePath()
{
	let currentPath;
	let path;

	if (window.location.origin === 'null') {
		// Local run
		const fullPath = window.location.href;
		const index = fullPath.indexOf('_build/html');
		currentPath = fullPath.substring(index);
		path = '_build/html/libc/functions/index.html';
	}
	else {
		// Server run
		currentPath = window.location.pathname;
		const pathSegments = currentPath.split('/').filter(segment => segment !== '');
		const firstItem = pathSegments[0] || null;

		if (firstItem === 'latest' || /^[0-9]+\.[0-9]+\.[0-9]+$/.test(firstItem)) {
			path = firstItem + '/libc/functions/index.html';
		}
		else {
			path = '/libc/functions/index.html';
		}
	}

	const fromSegments = currentPath.split('/');
	const toSegments = path.split('/');

	if (fromSegments.join() === toSegments.join()) {
		if (window.location.origin === 'null') {
			// Local run
			const fullPath = window.location.href;
			const index = fullPath.indexOf('_build/html');

			return fullPath.substring(0, index) + path;
		}
		else {
			// Server run
			return path;
		}
	}

	while (fromSegments[0] === toSegments[0]) {
		fromSegments.shift();
		toSegments.shift();
	}

	let relativePath = '';
	for (let i = 0; i < fromSegments.length - 1; i++) {
		relativePath += '../';
	}

	relativePath += toSegments.join('/');

	return relativePath;
}

function getElementsByTagNameWithDepth(element, tagName, depthLimit, currentDepth = 0)
{
	let elements = [];
	const children = element.children;

	for (let i = 0; i < children.length; i++) {
		const child = children[i];
		if (child.tagName.toLowerCase() === tagName.toLowerCase()) {
			elements.push(child);
		}

		if (currentDepth < depthLimit) {
			elements = elements.concat(getElementsByTagNameWithDepth(child, tagName, depthLimit, currentDepth + 1));
		}
	}

	return elements;
}

function removeCurrent(headersList)
{
	headersList.forEach(function(list) {
		if (list.classList.contains('current')) {
			list.querySelector('a').classList.remove('current');
			list.classList.remove('current');
			list.classList.remove('current-page');
			list.parentElement.classList.remove('current');
		}
	});
}

function triggerOpen(ul, label)
{
	const style = window.getComputedStyle(ul);
	const display = style.getPropertyValue('display');

	if (display !== 'block') {
		label.dispatchEvent(new MouseEvent('click', {
			view : window
		}));
	}
}

var anchors = document.getElementsByTagName('a');
var specificAnchor;

for (let i = 0; i < anchors.length; i++) {
	if (anchors[i].textContent === 'Functions') {
		specificAnchor = anchors[i];
		break;
	}
}

var functionsLi = specificAnchor.parentElement;

var headersLi = getElementsByTagNameWithDepth(functionsLi.querySelector('ul'), 'li', 1);

headersLi.forEach(function(list) {
	list.querySelector('a').addEventListener('click', function() {
		if (this.classList.contains('current')) {
			// Click on current element
			list.querySelector('label').dispatchEvent(new MouseEvent('click', {
				view : window
			}));
		}
		else {
			// Click on new element
			removeCurrent(headersLi);

			this.classList.add('current');
			list.classList.add('current');
			list.classList.add('current-page');
			list.parentElement.classList.add('current');

			triggerOpen(list.querySelector('ul'), list.querySelector('label'));
		}
	});

	const anchor = list.querySelector('a');
	// Slashes and dots in headers are replaced with '-'
	const textContent = anchor.textContent
		.replace(/\//g, '-')
		.replace(/\.h/g, '-h');

	const relativePath = findRelativePath() + '#' + textContent;

	anchor.setAttribute('href', relativePath);

	if (window.location.href.includes('#' + textContent)) {
		list.querySelector('a').classList.add('current');
		list.classList.add('current');
		list.classList.add('current-page');
		list.parentElement.classList.add('current');

		triggerOpen(list.querySelector('ul'), list.querySelector('label'));
	}
});
