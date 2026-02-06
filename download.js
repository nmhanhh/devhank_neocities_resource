const dlImg = document.querySelectorAll(".dlImg");

dlImg.forEach(img=>{
    img.addEventListener("click",()=>{
        const imgURL = img.dataset.url;
        const imgName = img.dataset.name;
        const link = document.createElement("a");
        link.href = imgURL;
        link.download = imgName;

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    })
});