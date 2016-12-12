tinymce.init({
    selector: 'textarea',
    height: 500,
    theme: 'modern',
    language: 'ru',
    language_url : '/static/grappelli/tinymce/jscripts/tiny_mce/langs/ru.js',
    plugins: [
        'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc'
    ],
    toolbar1: 'undo redo | insert | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
    toolbar2: 'print preview media | forecolor backcolor emoticons | codesample',
    image_advtab: true,
    templates: [
        {title: 'Test template 1', content: 'Test 1'},
        {title: 'Test template 2', content: 'Test 2'}
    ],
    content_css: [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i'
    ],
/*
    file_browser_callback: function(input_id, input_value, type, win){
        var cmsURL = '/admin/filebrowser/browse/?pop=4';
        cmsURL = cmsURL + '&type=' + type;

        tinymce.activeEditor.windowManager.open({
            file: cmsURL,
            width: 800,  // Your dimensions may differ - toy around with them!
            height: 500,
            resizable: 'yes',
            scrollbars: 'yes',
            inline: 'yes',  // This parameter only has an effect if you use the inlinepopups plugin!
            close_previous: 'no'
        }, {
            window: win,
            input: input_id
        });
        return false;
    }*/
});