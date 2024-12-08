const toggleBtn_1 = document.querySelector('#toggle-btn-1');
const toggleBtn_2 = document.querySelector('#toggle-btn-2');
const navLinks_1 = document.querySelector('#nav-links-1');
const navLinks_2 = document.querySelector('#nav-links-2');
const toggleImg_1 = document.querySelector('#toggle-img-1');
const toggleImg_2 = document.querySelector('#toggle-img-2');

const expandIcon = '/static/images/minus.png'; // 展開時的圖示
const collapseIcon = '/static/images/plus.png'; // 收合時的圖示

const histBtn = document.querySelector('#toggle-btn-hist');
const histLink = document.querySelector('#nav-links-hist');

function expand(navLink, img, icon) {
    navLink.classList.remove('hide');
    navLink.style.height = navLink.scrollHeight + 'px';
    img.src = icon;
}

function collapse(navLink, img, icon) {
    navLink.classList.add('hide');
    navLink.style.height = '0';
    img.src = icon;
}

let url_list = [
    "http://127.0.0.1:8000/", 
    "http://127.0.0.1:8000/users/login/", 
    "http://127.0.0.1:8000/users/register/", 
    "https://loglytics.ddns.net/", 
    "https://loglytics.ddns.net/users/login/",
    "https://loglytics.ddns.net/users/register/"
]

if (histBtn && histLink) {
    // 只有當 histBtn 和 histLink 存在時才執行以下代碼
    const askmeHeight = navLinks_1.scrollHeight;
    const histHeight = histLink.scrollHeight;

    const histExpandIcon = '/static/images/triangle-rotate.png'; // 展開時的圖示
    const histCollapseIcon = '/static/images/triangle.png'; // 收合時的圖示

    function expandAskme(navLink, img, icon) {
        navLink.classList.remove('hide');
        hist_session_state = sessionStorage.getItem('histNavState');
        if (hist_session_state === 'expanded') {
            navLink.style.height = askmeHeight + 'px';
        } else {
            h = askmeHeight -  histHeight;
            navLink.style.height = h + 'px';
        }
        img.src = icon;
    }

    function expandHist(navLink, navLinkHist, img, icon) {
        navLinkHist.classList.remove('hide');
        navLink.style.height = askmeHeight + 'px';
        navLinkHist.style.height = histHeight + 'px';
        img.src = icon;
    }

    function collapseHist(navLink, navLinkHist, img, icon) {
        navLinkHist.classList.add('hide');
        navLinkHist.style.height = '0';
        h = askmeHeight -  histHeight;
        navLink.style.height = h + 'px';
        img.src = icon;
    }

    if (url_list.includes(document.referrer)) {
        // 來自上面三個頁面
        collapseHist(navLinks_1, histLink, histBtn, histCollapseIcon);
        sessionStorage.setItem('histNavState', 'collapsed');

        expandAskme(navLinks_1, toggleImg_1, expandIcon);
        sessionStorage.setItem('navState_1', 'expanded');

        expand(navLinks_2, toggleImg_2, expandIcon);
        sessionStorage.setItem('navState_2', 'expanded');

    } else {
        // 非來自上面三個頁面就依之前的狀態
        session_state_1 = sessionStorage.getItem('navState_1');
        if (session_state_1 === 'collapsed') {
            // 如果之前收合，設置為隱藏
            collapse(navLinks_1, toggleImg_1, collapseIcon);
        } else {
            // 如果之前展開，設置為展開
            expandAskme(navLinks_1, toggleImg_1, expandIcon);
        }

        session_state_2 = sessionStorage.getItem('navState_2');
        if (session_state_2 === 'collapsed') {
            collapse(navLinks_2, toggleImg_2, collapseIcon);
        } else {
            expand(navLinks_2, toggleImg_2, expandIcon);
        }

        hist_session_state = sessionStorage.getItem('histNavState');
        if (hist_session_state === 'expanded') {
            expandHist(navLinks_1, histLink, histBtn, histExpandIcon);
        } else {
            const currentUrl = window.location.href;
            if (currentUrl === "http://127.0.0.1:8000/ask_me/cHistory/" || currentUrl === "https://loglytics.ddns.net/ask_me/cHistory/") {
                expandHist(navLinks_1, histLink, histBtn, histExpandIcon);
            } else {
                collapseHist(navLinks_1, histLink, histBtn, histCollapseIcon);
            }
        }
    }

    toggleBtn_1.addEventListener('click', () => {
        if (navLinks_1.classList.contains('hide')) {
            // 展開
            expandAskme(navLinks_1, toggleImg_1, expandIcon);
            sessionStorage.setItem('navState_1', 'expanded');
        } else {
            // 收合
            collapse(navLinks_1, toggleImg_1, collapseIcon);
            sessionStorage.setItem('navState_1', 'collapsed');
        } 
    });

    toggleBtn_2.addEventListener('click', () => {
        if (navLinks_2.classList.contains('hide')) {
            // 展開
            expand(navLinks_2, toggleImg_2, expandIcon);
            sessionStorage.setItem('navState_2', 'expanded');
        } else {
            // 收合
            collapse(navLinks_2, toggleImg_2, collapseIcon);
            sessionStorage.setItem('navState_2', 'collapsed');
        }
    });

    histBtn.addEventListener('click', (e) => {
        e.preventDefault();
        if (histLink.classList.contains('hide')) {
            // 展開
            expandHist(navLinks_1, histLink, histBtn, histExpandIcon);
            sessionStorage.setItem('histNavState', 'expanded');
        } else {
            // 收合
            collapseHist(navLinks_1, histLink, histBtn, histCollapseIcon);
            sessionStorage.setItem('histNavState', 'collapsed');
        }
    });

} else {
    if (url_list.includes(document.referrer)) {
        // 來自上面三個頁面
        expand(navLinks_1, toggleImg_1, expandIcon);
        sessionStorage.setItem('navState_1', 'expanded');

        expand(navLinks_2, toggleImg_2, expandIcon);
        sessionStorage.setItem('navState_2', 'expanded');
    } else {
        // 非來自上面三個頁面就依之前的狀態
        session_state_1 = sessionStorage.getItem('navState_1');
        if (session_state_1 === 'collapsed') {
            // 如果之前收合，設置為隱藏
            collapse(navLinks_1, toggleImg_1, collapseIcon);
        } else {
            // 如果之前展開，設置為展開
            expand(navLinks_1, toggleImg_1, expandIcon);
        }

        session_state_2 = sessionStorage.getItem('navState_2');
        if (session_state_2 === 'collapsed') {
            collapse(navLinks_2, toggleImg_2, collapseIcon);
        } else {
            expand(navLinks_2, toggleImg_2, expandIcon);
        }
    }

    toggleBtn_1.addEventListener('click', () => {
        if (navLinks_1.classList.contains('hide')) {
            // 展開
            expand(navLinks_1, toggleImg_1, expandIcon);
            sessionStorage.setItem('navState_1', 'expanded');
        } else {
            // 收合
            collapse(navLinks_1, toggleImg_1, collapseIcon);
            sessionStorage.setItem('navState_1', 'collapsed');
        } 
    });

    toggleBtn_2.addEventListener('click', () => {
        if (navLinks_2.classList.contains('hide')) {
            // 展開
            expand(navLinks_2, toggleImg_2, expandIcon);
            sessionStorage.setItem('navState_2', 'expanded');
        } else {
            // 收合
            collapse(navLinks_2, toggleImg_2, collapseIcon);
            sessionStorage.setItem('navState_2', 'collapsed');
        }
    });
}

