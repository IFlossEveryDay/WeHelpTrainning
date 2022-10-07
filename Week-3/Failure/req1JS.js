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
    // console.log(spotPics[0])
    // console.log(spotTitle[13])
    // let all = getSpot()
    // console.log(all)
    // let title1 = getSpot(0)
    // console.log(title1)
    // let title2 = getSpot(1)
    // console.log(title2)

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

    // =======Start of Title========
    let newTitle = document.createElement("div")
    newTitle.className = "title";
    let newTitleInside1 = document.createElement("div")
    newTitleInside1.className = "titleInside"
    let newTitleInside2 = document.createElement("div")
    newTitleInside2.className = "titleInside"
    let newTitleInside3 = document.createElement("div")
    newTitleInside3.className = "titleInside"
    let newTitleInside4 = document.createElement("div")
    newTitleInside4.className = "titleInside"
    let newTitleInside5 = document.createElement("div")
    newTitleInside5.className = "titleInside"
    let newTitleInside6 = document.createElement("div")
    newTitleInside6.className = "titleInside"
    let newTitleInside7 = document.createElement("div")
    newTitleInside7.className = "titleInside"
    let newTitleInside8 = document.createElement("div")
    newTitleInside8.className = "titleInside"

    let newTitPicContainer1 = document.createElement("div")
    newTitPicContainer1.className = "TitPicContainer"
    let newTitPicContainer2 = document.createElement("div")
    newTitPicContainer2.className = "TitPicContainer"
    let newTitPicContainer3 = document.createElement("div")
    newTitPicContainer3.className = "TitPicContainer"
    let newTitPicContainer4 = document.createElement("div")
    newTitPicContainer4.className = "TitPicContainer"
    let newTitPicContainer5 = document.createElement("div")
    newTitPicContainer5.className = "TitPicContainer"
    let newTitPicContainer6 = document.createElement("div")
    newTitPicContainer6.className = "TitPicContainer"
    let newTitPicContainer7 = document.createElement("div")
    newTitPicContainer7.className = "TitPicContainer"
    let newTitPicContainer8 = document.createElement("div")
    newTitPicContainer8.className = "TitPicContainer"
    //==== TITLEPICS====
    let newTitPic1 = document.createElement("img")
    newTitPic1.className = "TitPicAdj"
    newTitPic1.setAttribute("src", spotPics[2])
    let newTitPic2 = document.createElement("img")
    newTitPic2.className = "TitPicAdj"
    newTitPic2.setAttribute("src", spotPics[3])
    let newTitPic3 = document.createElement("img")
    newTitPic3.className = "TitPicAdj"
    newTitPic3.setAttribute("src", spotPics[4])
    let newTitPic4 = document.createElement("img")
    newTitPic4.className = "TitPicAdj"
    newTitPic4.setAttribute("src", spotPics[5])
    let newTitPic5 = document.createElement("img")
    newTitPic5.className = "TitPicAdj"
    newTitPic5.setAttribute("src", spotPics[6])
    let newTitPic6 = document.createElement("img")
    newTitPic6.className = "TitPicAdj"
    newTitPic6.setAttribute("src", spotPics[7])
    let newTitPic7 = document.createElement("img")
    newTitPic7.className = "TitPicAdj"
    newTitPic7.setAttribute("src", spotPics[8])
    let newTitPic8 = document.createElement("img")
    newTitPic8.className = "TitPicAdj"
    newTitPic8.setAttribute("src", spotPics[9])

    //==== TITLETEXT ====
    let newTit1 = document.createElement("div")
    newTit1.className = "titext"
    let spot3 = document.createTextNode(spotTitle[2])
    let newTit2 = document.createElement("div")
    newTit2.className = "titext"
    let spot4 = document.createTextNode(spotTitle[3])
    let newTit3 = document.createElement("div")
    newTit3.className = "titext"
    let spot5 = document.createTextNode(spotTitle[4])
    let newTit4 = document.createElement("div")
    newTit4.className = "titext"
    let spot6 = document.createTextNode(spotTitle[5])
    let newTit5 = document.createElement("div")
    newTit5.className = "titext"
    let spot7 = document.createTextNode(spotTitle[6])
    let newTit6 = document.createElement("div")
    newTit6.className = "titext"
    let spot8 = document.createTextNode(spotTitle[7])
    let newTit7 = document.createElement("div")
    newTit7.className = "titext"
    let spot9 = document.createTextNode(spotTitle[8])
    let newTit8 = document.createElement("div")
    newTit8.className = "titext"
    let spot10 = document.createTextNode(spotTitle[9])

    main.appendChild(newTitle)
    newTitle.appendChild(newTitleInside1)
    newTitleInside1.appendChild(newTitPicContainer1)
    newTitPicContainer1.appendChild(newTitPic1)
    newTitle.appendChild(newTitleInside2)
    newTitleInside2.appendChild(newTitPicContainer2)
    newTitPicContainer2.appendChild(newTitPic2)
    newTitle.appendChild(newTitleInside3)
    newTitleInside3.appendChild(newTitPicContainer3)
    newTitPicContainer3.appendChild(newTitPic3)
    newTitle.appendChild(newTitleInside4)
    newTitleInside4.appendChild(newTitPicContainer4)
    newTitPicContainer4.appendChild(newTitPic4)
    newTitle.appendChild(newTitleInside5)
    newTitleInside5.appendChild(newTitPicContainer5)
    newTitPicContainer5.appendChild(newTitPic5)
    newTitle.appendChild(newTitleInside6)
    newTitleInside6.appendChild(newTitPicContainer6)
    newTitPicContainer6.appendChild(newTitPic6)
    newTitle.appendChild(newTitleInside7)
    newTitleInside7.appendChild(newTitPicContainer7)
    newTitPicContainer7.appendChild(newTitPic7)
    newTitle.appendChild(newTitleInside8)
    newTitleInside8.appendChild(newTitPicContainer8)
    newTitPicContainer8.appendChild(newTitPic8)



    newTitleInside1.appendChild(newTit1)
    newTit1.appendChild(spot3)
    newTitleInside2.appendChild(newTit2)
    newTit2.appendChild(spot4)
    newTitleInside3.appendChild(newTit3)
    newTit3.appendChild(spot5)
    newTitleInside4.appendChild(newTit4)
    newTit4.appendChild(spot6)
    newTitleInside5.appendChild(newTit5)
    newTit5.appendChild(spot7)
    newTitleInside6.appendChild(newTit6)
    newTit6.appendChild(spot8)
    newTitleInside7.appendChild(newTit7)
    newTit7.appendChild(spot9)
    newTitleInside8.appendChild(newTit8)
    newTit8.appendChild(spot10)

    //===================== TESTS =========================
    //pro2
    // let pro2 = document.querySelector(".pro2")
    // let newPicContainer2 = document.createElement("div")
    // newPicContainer2.className = "picContainer2"
    // let newProPic2 = document.createElement("img")
    // newProPic2.className = "proPicAdj2"
    // newProPic2.setAttribute("src", spotPics[1])

    // let newPro2 = document.createElement("span")
    // newPro2.className = "proText2"
    // let spot2 = document.createTextNode(spotTitle[1])

    // pro2.appendChild(newPicContainer2)
    // newPicContainer2.appendChild(newProPic2)
    // pro2.appendChild(newPro2)
    // newPro2.appendChild(spot2)
    // =======End of Promotion========  


    // let proText2 = document.querySelector(".proText2")
    // let newPro2 = document.createElement("span")
    // let spot2 = document.createTextNode(spotTitle[1])
    // proText2.appendChild(newPro2)
    // newPro2.appendChild(spot2)

    // =======Start of titleInside========
    // let titext1 = document.querySelector(".titext1")
    // let newTit1 = document.createElement("div")
    // let spot3 = document.createTextNode(spotTitle[2])
    // titext1.appendChild(newTit1)
    // newTit1.appendChild(spot3)

    // let titext2 = document.querySelector(".titext2")
    // let newTit2 = document.createElement("div")
    // let spot4 = document.createTextNode(spotTitle[3])
    // titext2.appendChild(newTit2)
    // newTit2.appendChild(spot4)

    // let titext3 = document.querySelector(".titext3")
    // let newTit3 = document.createElement("div")
    // let spot5 = document.createTextNode(spotTitle[4])
    // titext3.appendChild(newTit3)
    // newTit3.appendChild(spot5)

    // let titext4 = document.querySelector(".titext4")
    // let newTit4 = document.createElement("div")
    // let spot6 = document.createTextNode(spotTitle[5])
    // titext4.appendChild(newTit4)
    // newTit4.appendChild(spot6)

    // let titext5 = document.querySelector(".titext5")
    // let newTit5 = document.createElement("div")
    // let spot7 = document.createTextNode(spotTitle[6])
    // titext5.appendChild(newTit5)
    // newTit5.appendChild(spot7)

    // let titext6 = document.querySelector(".titext6")
    // let newTit6 = document.createElement("div")
    // let spot8 = document.createTextNode(spotTitle[7])
    // titext6.appendChild(newTit6)
    // newTit6.appendChild(spot8)

    // let titext7 = document.querySelector(".titext7")
    // let newTit7 = document.createElement("div")
    // let spot9 = document.createTextNode(spotTitle[8])
    // titext7.appendChild(newTit7)
    // newTit7.appendChild(spot9)

    // let titext8 = document.querySelector(".titext8")
    // let newTit8 = document.createElement("div")
    // let spot10 = document.createTextNode(spotTitle[9])
    // titext8.appendChild(newTit8)
    // newTit8.appendChild(spot10)
})
