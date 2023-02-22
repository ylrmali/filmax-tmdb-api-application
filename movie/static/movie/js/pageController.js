const previousBtn = document.getElementById('previous');
const pages = document.getElementById('pages');

let currentUrl = window.location.search;
let urlParams = new URLSearchParams(currentUrl);
let page = parseInt(urlParams.get('page'));
let field = urlParams.get('field');


pageControlMenu();

function openPage(value){
    if (field === 'm'){
        window.location.href = `/movies?field=${field}&page=${value}`
    }
    else{
        window.location.href = `/series?field=${field}&page=${value}`
    }

}

function pageControlMenu(){
    for (let i = 1; i <= page; i++ ){
        pages.innerHTML += `<button class="page" onclick="openPage(this.innerHTML)">${i}</button>`
    }
}
function changePage(id){
    let movieUrl = '/movies?field=m&page=';
    let seriesUrl = '/series?field=s&page='
    if (id === 'next'){
        if (field === 'm'){
            window.location.href = `${movieUrl}${ page + 1}`;
        }
        else{
            window.location.href = `${seriesUrl}${ page + 1}`;
        }
    }
    if (id === 'previous'){
        if(page === 1){
            previousBtn.disabled = true;
        }
        else{
            if (field === 'm'){
                window.location.href = `${movieUrl}${ page - 1}`;
            }
            else{
                window.location.href = `${seriesUrl}${ page - 1}`;
            }
        }
    }
}




