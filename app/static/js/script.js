


/* link-path pour utiliser ckeditor-js --> (end-body) */
 {/* <script src="https://cdn.ckeditor.com/ckeditor5/38.0.1/classic/ckeditor.js"></script> */}



 /* ckeditor-js to class */
document.addEventListener('DOMContentLoaded', () => {
    const editors = document.querySelectorAll('textarea.ckeditor');

    if (editors.length === 0) return;

    editors.forEach(textarea => {
        ClassicEditor
            .create(textarea)
            .catch(console.error);
    });
});
