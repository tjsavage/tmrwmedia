$(document).ready(function() {
  // Code adapted from http://djangosnippets.org/snippets/1389/
 
  function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+-)');
    var replacement = prefix + '-' + ndx + '-';
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex,
 replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
  }
 
  function deleteForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
 
    if (formCount > 1) {
      // Delete the item/form
      $(btn).parents('.item').remove();
 
      var forms = $('.item'); // Get all the forms
 
      // Update the total number of forms (1 less than before)
      $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
 
      var i = 0;
      // Go through the forms and set their indices, names and IDs
      for (formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).children().children().each(function() {
          updateElementIndex(this, prefix, i);
        });
      }
 
    } // End if
    else {
        alert("You have to enter at least one group!");
    }
    return false;
  }
 
  function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
 
      // Clone a form (without event handlers) from the first form
      var row = $(".item:first").clone(false).get(0);
      // Insert it after the last form
      $(row).removeAttr('id').hide().insertAfter(".item:last").slideDown(300);
 
      // Remove the bits we don't want in the new row/form
      // e.g. error messages
      $(".errorlist", row).remove();
      $(row).children().removeClass("error");
 
      // Relabel or rename all the relevant bits
      $(row).children().children().each(function() {
        updateElementIndex(this, prefix, formCount);
        $(this).val("");
      });
 
      // Add an event handler for the delete item/form link
      $(row).find(".delete").click(function() {
        return deleteForm(this, prefix);
      });
 
      // Update the total form count
      $("#id_" + prefix + "-TOTAL_FORMS").val(formCount + 1); 
 
   
    return false;
  }
 
  // Register the click event handlers
  $("#add").click(function() {
    return addForm(this, "form");
  });
 
  $(".delete").click(function() {
    return deleteForm(this, "form");
  });
  
  $("#formset-form").submit(function() {
  	 var forms = $('.item'); // Get all the forms
 
      var i = 0;
      // Go through the forms and delete the ones without names
      for (formCount = forms.length; i < formCount; i++) {
      	if($(forms.get(i)).find("#id_form-" + i + "-name").val() == ""){
      		deleteForm($(forms.get(i)).find(".delete"), "form");
      	}
      }
      
      return true;
    });
  	
  	
 
});