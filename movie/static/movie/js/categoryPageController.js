// urldeki gerekli parametreleri aldık.
let url = window.location.search;
let urlParams = new URLSearchParams(url);
let type = urlParams.get('type');
let page = parseInt(urlParams.get('page'));
let category = urlParams.get('category');
const previousBtn = document.getElementById('previous');
const pages = document.getElementById('pages');

pageControlMenu();

function openPage(value){
    window.location.href = `/movies/categories?type=${type}&page=${value}&category=${category}`
}

function pageControlMenu(){
    for (let i = 1; i <= page; i++ ){
        pages.innerHTML += `<button class="page" onclick="openPage(this.innerHTML)">${i}</button>`
    }
}

function categoryChangePage(id){
    let movieUrl = `/movies/categories?type=m&page=${page}&category=${category}`;
    let seriesUrl = `/series/categories?type=s&page=${page}&category=${category}`;

    if (id === 'next'){
        if (type === 'm'){
            window.location.href = `/movies/categories?type=m&page=${page + 1}&category=${category}`;
        }
        else{
            window.location.href = `/series/categories?type=s&page=${page + 1}&category=${category}`;
        }
    }
    if (id === 'previous'){
        if(page === 1){
            previousBtn.disabled = true;
        }
        else{
            if (type === 'm'){
                window.location.href = `/movies/categories?type=m&page=${page - 1}&category=${category}`;
            }
            else{
                window.location.href = `/series/categories?type=s&page=${page - 1}&category=${category}`;
            }
        }
    }
}