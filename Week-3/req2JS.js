let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
fetch(src).then(function (response) {
    return response.json();
}).then(function (tpeAttractions) {


    let attractions;
    let tpe = tpeAttractions.result.results;
    // console.log("資料為", tpe);
    function getSpot() {
        let spotsArr = []
        for (let i = 0; i < tpe.length; i++) {
            attractions = tpe[i];
            let spots = attractions.stitle
            // console.log(attractions.stitle)
            spotsArr.push(spots)
            // console.log(spots)
        }
        return spotsArr

    }

    function getPics() {
        let picUrl;
        let picSep;
        let firstPic;
        let picArr = [];
        for (let i = 0; i < tpe.length; i++) {
            pics = tpe[i]
            picUrl = pics.file
            picSep = picUrl.split("https", 2)
            firstPic = "https" + picSep[1]
            picArr.push(firstPic)

        }

        return picArr
    }

    let spotTitle = getSpot()
    let spotPics = getPics()

    // =======Start of Promotion========
    let main = document.querySelector(".main")
    main.className = "main"
    let newPromotion = document.createElement("div")
    newPromotion.className = "promotion"
    let newPro1 = document.createElement("div")
    newPro1.className = "pro1"

    let newPro2 = document.createElement("div")
    newPro2.className = "pro2"

    let newPicContainer1 = document.createElement("div")
    newPicContainer1.className = "picContainer"

    let newPicContainer2 = document.createElement("div")
    newPicContainer1.className = "picContainer"

    let newProPic1 = document.createElement("img")
    newProPic1.className = "proPicAdj1"

    let newProPic2 = document.createElement("img")
    newProPic2.className = "proPicAdj2"

    newProPic1.setAttribute("src", spotPics[0])
    newProPic2.setAttribute("src", spotPics[1])

    let newProText1 = document.createElement("span")
    newProText1.className = "proText1"
    let newProText2 = document.createElement("span")
    newProText2.className = "proText2"

    let spot1 = document.createTextNode(spotTitle[0])
    let spot2 = document.createTextNode(spotTitle[1])

    main.appendChild(newPromotion)
    newPromotion.appendChild(newPro1)
    newPro1.appendChild(newPicContainer1)
    newPicContainer1.appendChild(newProPic1)

    newPromotion.appendChild(newPro2)
    newPro2.appendChild(newPicContainer2)
    newPicContainer2.appendChild(newProPic2)


    newPro1.appendChild(newProText1)
    newProText1.appendChild(spot1)
    newPro2.appendChild(newProText2)
    newProText2.appendChild(spot2)
    // =======End of Promotion========

    //============  Start of Title  ======================
    let newTitle = document.createElement("div")
    newTitle.className = "title";


    for (i = 2; i < 10; i++) {
        let newTitleInside = document.createElement("div")
        newTitleInside.className = "titleInside"

        let newTitPicContainer = document.createElement("div")
        newTitPicContainer.className = "TitPicContainer"
        let newTitPic = document.createElement("img")
        newTitPic.className = "TitPicAdj"
        newTitPic.setAttribute("src", spotPics[i])

        let newTit = document.createElement("div")
        newTit.className = "titext"
        let spot = document.createTextNode(spotTitle[i])

        main.appendChild(newTitle)
        newTitle.appendChild(newTitleInside)
        newTitleInside.appendChild(newTitPicContainer)
        newTitPicContainer.appendChild(newTitPic)

        main.appendChild(newTitle)
        newTitle.appendChild(newTitleInside)
        newTitleInside.appendChild(newTit)
        newTit.appendChild(spot)

    }
})
