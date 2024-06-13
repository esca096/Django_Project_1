const loginForm = document.getElementById('login-form');
const baseEndpoint = "http://localhost:8080/api";
const productList = document.getElementById('product-list');

if (loginForm){
    loginForm.addEventListener('submit', handleLogin);
}

function handleLogin(event){

    event.preventDefault();

    const loginEndpoint = `${baseEndpoint}/token/`;

    let loginFormData = new FormData(loginForm);

    let loginBjectData = Object.fromEntries(loginFormData);

    let bodyJsonData = JSON.stringify(loginBjectData);

    const options = {
        method:"POST",
        headers:{
            "Content-type":"application/json"
        },
        body: bodyJsonData
    }
    
    fetch(loginEndpoint, options) // requests.post(endpoint, data) --> promise
    .then(response =>{
        console.log(response);
        return response.json();
    })
    .then(authData =>{
        handleAuthData(authData, getProductLIst);
    })
    .catch(err =>{
        console.log('error', err);
    })
    
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access);
    localStorage.setItem('refresh', authData.refresh);
    if (callback){
        callback();
    }
}


function writeToconatainer(data){
    if(productList){
        productList.innerHTML = '<pres>' + JSON.stringify(data,null,4) + "</pres>";
    }
}

function getProductLIst(){
    const endpoint = `${baseEndpoint}/create/`;
    const options ={
        method: 'GET',
        headers:{
            'Content-type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        }
    }
    fetch(endpoint, options)
    .then(response =>response.json())
    .then(data =>{
        writeToconatainer(data);
    })

}