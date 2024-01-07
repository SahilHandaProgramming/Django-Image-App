let categoryMain = document.querySelector(".category-btn");
let categoryChild = document.querySelector(".category-box")

categoryMain.addEventListener('click',(e)=>{
    e.preventDefault()
     categoryChild.classList.toggle("category-box")
    // alert("Hello")
})