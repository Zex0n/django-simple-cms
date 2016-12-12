function CustomFileBrowser(input_id, input_value, type, win){
    var cmsURL = '/admin/filebrowser/browse/?pop=4';
    cmsURL = cmsURL + '&type=' + type;

    tinymce.activeEditor.windowManager.open({
        file: cmsURL,
        width: 1024,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'yes',  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: 'no'
    }, {
        window: win,
        input: input_id,
    });
    return false;
}


tinymce.init({
  selector: "#id_text",
  height: 400,
  plugins: [
    "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
    "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
    "table contextmenu directionality emoticons template textcolor paste fullpage textcolor colorpicker textpattern"
  ],

  toolbar1: "bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | styleselect formatselect fontselect fontsizeselect",
  toolbar2: "cut copy paste | searchreplace | bullist numlist | outdent indent blockquote | undo redo | link unlink anchor image media code | insertdatetime preview | forecolor backcolor",
  toolbar3: "table | hr removeformat | subscript superscript | charmap emoticons | print fullscreen | ltr rtl | spellchecker | visualchars visualblocks nonbreaking template pagebreak restoredraft",

  menubar: true,
  toolbar_items_size: 'small',
  language: 'ru',

  // Callbacks
  file_browser_callback: 'CustomFileBrowser',

  image_advtab: false,
  extended_valid_elements: 'iframe[src|title|width|height|allowfullscreen|frameborder|class|id],object[classid|width|height|codebase|*],param[name|value|_value|*],embed[type|width|height|src|*]"',
  file_browser_callback: CustomFileBrowser,
  convert_urls : false,

  style_formats: [{
    title: 'Bold text',
    inline: 'b'
  }, {
    title: 'Red text',
    inline: 'span',
    styles: {
      color: '#ff0000'
    }
  }, {
    title: 'Red header',
    block: 'h1',
    styles: {
      color: '#ff0000'
    }
  }, {
    title: 'Example 1',
    inline: 'span',
    classes: 'example1'
  }, {
    title: 'Example 2',
    inline: 'span',
    classes: 'example2'
  }, {
    title: 'Table styles'
  }, {
    title: 'Table row 1',
    selector: 'tr',
    classes: 'tablerow1'
  }],

  init_instance_callback : function(editor) {
        django.jQuery('.mce-tinymce').prev('label').css('width', '100%').css('float', 'none');
   }

});


(function($) { // < start of closure
    // within this block, $ = django.jQuery
    $(document).ready(function() {

    });
})(django.jQuery); // passes django.jQuery as parameter to closure block