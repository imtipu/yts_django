"use-strict"

$(document).ready(function () {
   $('.download-modal').on('click', function () {
       let html = $('#downloadModal .modal-body .download-buttons tbody');
       html.html('');
       let id = $(this).data('id');
       $.ajax({
           url: 'https://yts.mx/api/v2/movie_details.json?movie_id=' + id.toString(),
       }).done(function (data) {

           let torrents = data.data.movie.torrents;
           let i;
           for (i = 1; i < torrents.length; i++){
               let row = '<tr>' +
                   '<th scope="row">'+i+'</th>' +
                   '<td>'+torrents[i].type+'</td>' +
                   '<td>'+torrents[i].quality+'</td>' +
                   '<td>'+torrents[i].size+'</td>' +
                   '<td><a class="btn-download" href="'+torrents[i].url+'">Download</a></td>'+
                    '</tr>';
               html.append(row)
           }
           $('#downloadModal').modal('show');

       })
   })
});