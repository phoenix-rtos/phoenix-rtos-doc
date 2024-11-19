const curr_version = document.querySelector('.curr-version');
const currentPath = window.location.pathname;
const pathSegments = currentPath.split('/').filter(segment => segment !== '');
const firstItem = pathSegments[0] || null;

if (firstItem !== null &&
   (/^[0-9]+\.[0-9]+\.[0-9]+$/.test(firstItem)))
{
    curr_version.textContent = 'ver. ' + firstItem;
}
// version directories not available - marking the current version as latest
else {
    curr_version.textContent = 'ver. latest';
}

const versions = document.querySelector('.other-versions');

versions.querySelectorAll('a').forEach(anchor => {
    anchor.addEventListener('click', function() {
        baseTag.href = window.location.origin + anchor.textContent + '/';
    });
});

const triggerElement = document.querySelector('.default-version');
const versionContainer = document.querySelector('.version-container');
const sidebarContainer = document.querySelector('.sidebar-container');

triggerElement.addEventListener('click', function() {
    versionContainer.classList.toggle('shift-up');
});
