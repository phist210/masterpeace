//may need to initialize feedback 1-5 at 0, feedback is apart of the serializer.
//file to create a new image masterpeace post

function createImage(event) {
    event.preventDefault();
    console.log("create");
    $form = {
      'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
      'tag': $('[name="tag"]').val(),
      'owner': $('[name="owner"]').val(),
      'image': $('[name="form-image"]').val(),
      'artform': $('[name="artform"]').val(),
      'caption': $('[name="caption"]').val(),
      'allow_feedback': true,
      'feedback1': 0,
      'feedback2': 0,
      'feedback3': 0,
      'feedback4': 0,
      'feedback5': 0,
    }
    console.log($form);
    $.ajax({
        method: 'POST',
        url: "/api/image_mp/",
        data: $form,
        success: function(result) {
            console.log('success');
        }
    });
}

console.log('hi there line 10');
$('#submitBtn').click(createImage);