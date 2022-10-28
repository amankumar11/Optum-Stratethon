var arr1 = [];
function getSelectedItems(el){
    var e = document.getElementById('symptoms');
    var strSel =e.options[e.selectedIndex].text;

    arr1.push(strSel);
    console.log(arr1);

}