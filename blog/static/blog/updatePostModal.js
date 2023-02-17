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
    // console.log("hodsfj;alkfdj;asldkj")
    // this in a url suggests an attempt to update a post
    // this url is pushing the instance info to the modal through django
    const modalAnchor = document.querySelector('#updateModalAnchor')
    if(window.location.href.indexOf("updatePost") > 1){
        $("#updatePostModal").modal('show')
    }
    $("#updatePostModal").on('hidden.bs.modal', function(e){
        console.log("hello")
        location.href = modalAnchor.dataset.home
        
    })

    const addPostButton = document.querySelector('#addPostButton')
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
