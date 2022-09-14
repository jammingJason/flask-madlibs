btnAddItem = document.querySelector('#addItem')
btnCreateMadlib = document.querySelector('#subitMadlib')
strValue = document.querySelector('#txtArea')
strItem = document.querySelector('#txtItem')
strWords = document.querySelector('#txtWords')
arrItems = []
btnAddItem.addEventListener('click', function(evt){
    evt.preventDefault()
    strMadlib = strValue.value + ' {' +strItem.value.toLowerCase()+'} '
    strValue.value = strMadlib
    arrItems.push(strItem.value.toLowerCase())
    strItem.value = ''
    // alert(arrItems)
})


btnCreateMadlib.addEventListener('click', function(evt){
    evt.preventDefault()
    strWords.value = arrItems
    document.frmMain.submit()
})