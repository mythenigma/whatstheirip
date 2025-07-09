// Existing script for tracking code input
$("#joeresult").
  on("blur", function () {
    doCode();
  }).
  on("keydown", function (e) {
    if (e.keyCode == 13) {
      doCode();
    }
  });

function doCode() {
  var resu = document.getElementById("joeresult");
  // var resu=resu.value;
  // document.getElementById("resultlink").innerHTML="Click Link to View Result: <br>"+"<a href=https://grabify.icu/"+resu+" target=\"_blank\">https://grabify.icu/"+resu+"</a>";
}

// Slider for email tracker
$('#myRange2').mousemove(function() {
  if($('#myRange2').val()==100){
    document.getElementById("rangeValue2").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue2").innerHTML="Drag Progress Bar to the End";
  }
});

document.getElementById("myRange2").addEventListener('touchend', function(){
  if($('#myRange2').val()==100){
    document.getElementById("rangeValue2").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue2").innerHTML="Drag Progress Bar to the End";
  }
});

document.getElementById("myRange2").addEventListener('touchmove', function(){
  if($('#myRange2').val()==100){
    document.getElementById("rangeValue2").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue2").innerHTML="Drag Progress Bar to the End";
  }
});

// Slider for URL tracker
$('#myRange').mousemove(function(){
  if($('#myRange').val()==100){
    document.getElementById("rangeValue").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue").innerHTML="Drag Progress Bar to the End";
  }
});

document.getElementById("myRange").addEventListener('touchend', function(){
  if($('#myRange').val()==100){
    document.getElementById("rangeValue").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue").innerHTML="Drag Progress Bar to the End";
  }
});

document.getElementById("myRange").addEventListener('touchmove', function(){
  if($('#myRange').val()==100){
    document.getElementById("rangeValue").innerHTML="You're Good to Go";
  } else {
    document.getElementById("rangeValue").innerHTML="Drag Progress Bar to the End";
  }
});

// Initialize QR code generator
var qrcode2 = new QRCode(document.getElementById("qrcodeweb"), {
  width: 170,
  height: 170,
  colorDark: "#000000",
  colorLight: "#ffffff",
  correctLevel: QRCode.CorrectLevel.H
});

// Generate URL tracking code
async function makeCodeweb() {
  document.getElementById("btypesay").innerHTML='<div class="spinner-grow text-primary mx-1"></div><div class="spinner-grow text-primary mx-1"></div><div class="spinner-grow text-primary mx-1"></div>';
  var web = document.getElementById("webinput");
  
  if(web.value.length<10){
    alert('Please enter a valid URL');
    return;
  }
  
  let filterstrings = ['porn','redtube','81ea'];
  let regex = new RegExp(filterstrings.join("|"), "i");  
  if(regex.test(web.value)){
    alert('That content is not allowed'); 
    return 0;
  }

  if($('#myRange').val()==100){
    var ranger20 = document.getElementById("myRange");
    ranger20.value=20;
    document.getElementById("rangeValue").innerHTML="Drag Progress Bar to the End";
  } else {
    alert('Please drag the progress bar to the end');
    return;
  }
  
  qrcode2.makeCode(web.value);
  const data = new FormData();
  data.append('i', web.value);
  const response = await fetch("https://grabify.icu/qrcode.php", {
    method: "POST",
    body: data
  });
  
  try {
    const res = await response.text().then(text => text.trim());
    continuewithcode(res);
  } catch (error) {
    return;
  }
}

async function continuewithcode(res){
  if (res.includes("Reachable")) {
    alert('Please enter a valid URL');
    return;
  }
  
  res = res.split(":");
  $("#xingxi").fadeOut("slow");
  var qd ="https://grabb.site/"+res[1];
  qrcode2.makeCode(qd);
  
  // Populate the always-visible black input boxes
  document.getElementById("immediateTrackingUrl").textContent = qd;
  document.getElementById("immediateTrackingCode").textContent = res[2];
  
  // Show the "View Results" button
  document.getElementById("viewTrackingData").href = `https://grabify.icu/${res[2]}`;
  document.getElementById("viewTrackingData").style.display = "inline-block";
  
  // Also populate the original detailed section
  document.getElementById("atype").innerHTML="<strong>New Tracking Link:</strong> <br>"+"<a href=https://grabb.site/"+res[1]+" target=\"_blank\" class=\"btn btn-sm btn-outline-primary mt-2\"><i class=\"fas fa-external-link-alt mr-1\"></i> https://grabb.site/"+res[1]+"</a>";
  document.getElementById("btypesay").innerHTML="<strong>Tracking Code:</strong> "+res[2];
  document.getElementById("btype").innerHTML="<strong>Tracking Results:</strong> <br>"+"<a href=https://grabify.icu/"+res[2]+" target=\"_blank\" class=\"btn btn-sm btn-outline-primary mt-2\"><i class=\"fas fa-chart-line mr-1\"></i> View Tracking Data</a>";
  $("#xingxi").fadeIn("slow");
}

// Generate email tracking code
async function continuewithcode2(res){
  if (res.includes("Reachable")) {
    alert('An error occurred');
    return;
  }
  
  res = res.split(":");
  const trackingImageUrl = "https://grabb.site/wx/"+res[1]+".png";
  const trackingCode = res[2];
  const trackingResultsUrl = "https://grabify.icu/"+res[2];
  
  // Update the tracking pixel image
  document.getElementById("tpng").src = trackingImageUrl;
  
  // Populate the always-visible email tracking boxes
  document.getElementById("immediateEmailTrackingUrl").textContent = trackingImageUrl;
  document.getElementById("immediateEmailTrackingCode").textContent = trackingCode;
  
  // Show the "View Results" button and set its URL
  const viewEmailButton = document.getElementById("viewEmailTrackingData");
  viewEmailButton.href = trackingResultsUrl;
  viewEmailButton.style.display = "inline-block";
  
  // Update the existing legacy elements for backward compatibility
  document.getElementById("aer").innerHTML="<strong>Email Tracker Image:</strong> <br>"+"<a href="+trackingImageUrl+" target=\"_blank\" class=\"btn btn-sm btn-outline-primary mt-2\"><i class=\"fas fa-image mr-1\"></i> "+trackingImageUrl+"</a>";
  document.getElementById("bsay").innerHTML="<strong>Tracking Code:</strong> "+trackingCode;
  document.getElementById("ber").innerHTML="<strong>Tracking Results:</strong> <br>"+"<a href="+trackingResultsUrl+" target=\"_blank\" class=\"btn btn-sm btn-outline-primary mt-2\"><i class=\"fas fa-chart-line mr-1\"></i> View Tracking Data</a>";
  
  // Show success notification
  showToast('Email tracking pixel generated successfully!', 'success');
}

async function makeCodeweb2() {
  document.getElementById("bsay").innerHTML="<div class=\"spinner-grow text-primary mx-1\"></div><div class=\"spinner-grow text-primary mx-1\"></div><div class=\"spinner-grow text-primary mx-1\"></div>";
  
  if($('#myRange2').val()==100){
    var ranger20 = document.getElementById("myRange2");
    ranger20.value=20;
    document.getElementById("rangeValue2").innerHTML="Drag Progress Bar to the End";
  } else {
    alert('Please drag the progress bar to the end');
    return;
  }
  
  const data = new FormData();
  data.append('i', 'mm');
  const response = await fetch("https://grabify.icu/qrcode.php", {
    method: "POST",
    body: data
  });
  
  try {
    const res = await response.text().then(text => text.trim());
    continuewithcode2(res);
  } catch (error) {
    return;
  }
}

function myFunctionpic() {
  var copyText = document.getElementById("webinputpic");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  document.getElementById("Copied").innerHTML = "Copied";
}

// Add smooth scrolling
$(document).ready(function() {
  // Add smooth scrolling to all links
  $("a.js-scroll-trigger").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top - 70
      }, 800);
    }
  });
  
  // Close responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });
  
  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 75
  });
});

// Show toast notification
function showToast(message, type = 'success') {
  // Create toast element
  const toast = document.createElement('div');
  toast.className = `toast align-items-center text-white bg-${type === 'success' ? 'success' : 'danger'} border-0`;
  toast.setAttribute('role', 'alert');
  toast.setAttribute('aria-live', 'assertive');
  toast.setAttribute('aria-atomic', 'true');
  toast.style.position = 'fixed';
  toast.style.top = '20px';
  toast.style.right = '20px';
  toast.style.zIndex = '9999';
  toast.style.minWidth = '300px';
  
  toast.innerHTML = `
    <div class="d-flex">
      <div class="toast-body">
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'} mr-2"></i>
        ${message}
      </div>
      <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
  `;
  
  // Add to page
  document.body.appendChild(toast);
  
  // Initialize and show toast
  const bsToast = new bootstrap.Toast(toast, {
    autohide: true,
    delay: 3000
  });
  bsToast.show();
  
  // Remove from DOM after hiding
  toast.addEventListener('hidden.bs.toast', function () {
    document.body.removeChild(toast);
  });
}

// Copy text from an element by ID
function copyFromElement(elementId, successMessage = 'Copied to clipboard!') {
  try {
    const element = document.getElementById(elementId);
    if (!element) {
      alert('Element not found');
      return;
    }
    
    const text = element.textContent || element.innerText;
    if (!text || text.trim() === '' || text.includes('will appear here')) {
      alert('No content to copy yet. Please generate a tracking link first.');
      return;
    }
    
    // Create a temporary textarea to copy the text
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, 99999);
    
    const successful = document.execCommand('copy');
    document.body.removeChild(textarea);
    
    if (successful) {
      // Show success message briefly
      const originalButton = event.target.closest('button');
      if (originalButton) {
        const originalContent = originalButton.innerHTML;
        originalButton.innerHTML = '<i class="fas fa-check mr-1"></i>Copied!';
        originalButton.classList.add('btn-success');
        setTimeout(() => {
          originalButton.innerHTML = originalContent;
          originalButton.classList.remove('btn-success');
        }, 2000);
      } else {
        alert(successMessage);
      }
    } else {
      alert('Failed to copy to clipboard');
    }
  } catch (error) {
    console.error('Copy failed:', error);
    alert('Copy failed: ' + error.message);
  }
}

// Generate tracking link from user input tracking code
function generateTrackingLink() {
  const trackingCode = document.getElementById('trackingCodeInput').value.trim();
  const linkSection = document.getElementById('generatedLinkSection');
  const linkElement = document.getElementById('generatedTrackingLink');
  const viewButton = document.getElementById('viewGeneratedTrackingData');
  const feedback = document.getElementById('trackingCodeFeedback');
  
  if (trackingCode === '') {
    linkSection.style.display = 'none';
    feedback.style.display = 'none';
    return;
  }
  
  // Validate tracking code format (basic validation)
  const isValidFormat = trackingCode.length >= 3 && /^[a-zA-Z0-9]+$/.test(trackingCode);
  
  if (isValidFormat) {
    feedback.style.display = 'block';
    
    // Generate the complete tracking link
    const fullTrackingLink = `https://grabify.icu/${trackingCode}`;
    linkElement.textContent = fullTrackingLink;
    
    // Update the view results link
    viewButton.href = `https://grabify.icu/track/${trackingCode}`;
    
    // Show the results section
    linkSection.style.display = 'block';
    
    // Show success toast only once when a valid code is first detected
    if (trackingCode.length >= 3) {
      // Clear any previous timeout
      if (window.toastTimeout) {
        clearTimeout(window.toastTimeout);
      }
      // Set a small delay to avoid showing toast on every keystroke
      window.toastTimeout = setTimeout(() => {
        showToast('Tracking link generated successfully!', 'success');
      }, 1000);
    }
  } else {
    feedback.style.display = 'none';
    linkSection.style.display = 'none';
  }
}
