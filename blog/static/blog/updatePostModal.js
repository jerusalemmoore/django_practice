// function updatePostModalButton(postid){
//     $("#updatePostModalButton").click(function(e){
//         e.preventDefault();
//         $.ajax({
//             method: "POST",
//             url: 'home',
//             data: {
//                 postid: postid,
//             }
//         },
//         // success: function(result){
//         //     alert('ok');
//         // },
//         // error: function(result) {
//         //     alert('error');
//         // }
//         );
//     });
// }
function getCookie(){
    docCookie = document.cookie
    splitString = docCookie.split("=")
    cookie = splitString[splitString.length -1]
    console.log(cookie)
    return cookie
}
// $(document).ready(function () {
    // e.preventDefault();
// function modalButton(){

   

            
// }

$(document).ready(function () {
    console.log("hodsfj;alkfdj;asldkj")
    if(window.location.href.indexOf("updatePost") > 1){
        $("#updatePostModal").modal('show')
    }
})
    // $('#updatePostModalButton').click(function () {
    //     var postid = $(this).attr("data-postid");
    //     console.log("hello")
    //     console.log(document.cookie)
    //     console.log(typeof $(this).attr("data-fullpath"))
    //     console.log(postid)
    //     myurl = $(this).attr("data-fullpath").trim() + "/" + postid.toString().trim()
    //     console.log(myurl)
    //     $.ajax(
    //         {
    //             headers: {
    //                 "X-CSRFToken": getCookie()
    //             },
    //             type: "POST",
    //             url: myurl,
    //             data: {
    //                 post_id: postid
    //             },
    //             success: function (data) {
                    
    //             }
    //         }
    //     )
    // }
//     );
// }
// )
