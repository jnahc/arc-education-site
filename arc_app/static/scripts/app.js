console.log('hello there')

// $btn = $('.btn')
// $btn.hover(function(){
//     console.log('A');
//     $btn.toggleClass('animated pulse')
//     }, function(){
//     console.log('B');
//     $btn.toggleClass('animated pulse');
//     }
// );

$btnMyProfile = $('.btn:contains("My Profile")')
$btnMyProfile.hover(function(){
    console.log('C');
    $btnMyProfile.toggleClass('animated heartBeat')
    }, function(){
    console.log('D');
    $btnMyProfile.toggleClass('animated heartBeat');
    }
);

$btnSignUp = $(`.btn:contains("Sign up")`)
$btnSignUp.hover(function(){
    console.log('C');
    $btnSignUp.toggleClass('animated bounce')
    }, function(){
    console.log('D');
    $btnSignUp.toggleClass('animated bounce');
    }
);

$btnLogIn = $(`.btn:contains("Login")`)
$btnLogIn.hover(function(){
    console.log('C');
    $btnLogIn.toggleClass('animated rubberBand')
    }, function(){
    console.log('D');
    $btnLogIn.toggleClass('animated rubberBand');
    }
);

$btnRegister = $(`.btn:contains("Register")`)
$btnRegister.hover(function(){
    console.log('C');
    $btnRegister.toggleClass('animated tada')
    }, function(){
    console.log('D');
    $btnRegister.toggleClass('animated tada');
    }
);

$logoTop = $(`#topnav-brand:contains("ARC")`)
$logoTop.hover(function(){
    console.log('C');
    $logoTop.toggleClass('animated jello')
    }, function(){
    console.log('D');
    $logoTop.toggleClass('animated jello');
    }
);

$logoBottom = $(`#bottomnav-brand:contains("ARC")`)
$logoBottom.hover(function(){
    console.log('C');
    $logoBottom.toggleClass('animated lightSpeedOut')
    }, function(){
    console.log('D');
    $logoBottom.toggleClass('animated lightSpeedOut');
    }
);

$navLinkHome = $(`.nav-link:contains("Home")`)
$navLinkHome.hover(function(){
    console.log('C');
    $navLinkHome.toggleClass('animated fadeOutDown')
    }, function(){
    console.log('D');
    $navLinkHome.toggleClass('animated fadeOutDown');
    }
);

$navLinkCourses = $(`.nav-link:contains("Courses")`)
$navLinkCourses.hover(function(){
    console.log('C');
    $navLinkCourses.toggleClass('animated fadeOutLeft')
    }, function(){
    console.log('D');
    $navLinkCourses.toggleClass('animated fadeOutLeft');
    }
);

$navLinkAbout = $(`.nav-link:contains("About Us")`)
$navLinkAbout.hover(function(){
    console.log('C');
    $navLinkAbout.toggleClass('animated fadeOutRight')
    }, function(){
    console.log('D');
    $navLinkAbout.toggleClass('animated fadeOutRight');
    }
);

$navLinkRegister = $(`.nav-link:contains("Register")`)
$navLinkRegister.hover(function(){
    console.log('C');
    $navLinkRegister.toggleClass('animated flipOutX')
    }, function(){
    console.log('D');
    $navLinkRegister.toggleClass('animated flipOutX');
    }
);

$navLinkLogin = $(`.nav-link:contains("Login")`)
$navLinkLogin.hover(function(){
    console.log('C');
    $navLinkLogin.toggleClass('animated flipOutY')
    }, function(){
    console.log('D');
    $navLinkLogin.toggleClass('animated flipOutY');
    }
);

$navBottomText = $(`.navbar-text:contains("Copyright")`)
$navBottomText.hover(function(){
    console.log('C');
    $navBottomText.toggleClass('animated flash')
    }, function(){
    console.log('D');
    $navBottomText.toggleClass('animated flash');
    }
);

$aLogin = $('.A-login');
$rLogin = $(`.R-login`);
$cLogin = $(`.C-login`);

$aLogin.click(function(){
    console.log('C');
    $aLogin.toggleClass('animated zoomOutLeft');
    }
);
$rLogin.click(function(){
    console.log('C');
    $rLogin.toggleClass('animated zoomOut');
    }
);
$cLogin.click(function(){
    console.log('C');
    $cLogin.toggleClass('animated zoomOutRight');
    }
);

$kennyPic = $('#kenny-pic');
$jeffPic = $('#jeff-pic');
$felipePic = $('#felipe-pic');
$pouyeshPic = $('#pouyesh-pic');

$kennyPara = $('#kenny-para');
$jeffPara = $('#jeff-para');
$felipePara = $('#felipe-para');
$pouyeshPara = $('#pouyesh-para');

$kennyPic.click(function(){
    console.log('C');
    $kennyPara.toggleClass('animated lightSpeedOut');
    }
);
$jeffPic.click(function(){
    console.log('C');
    $jeffPara.toggleClass('animated hinge');
    }
);
$felipePic.click(function(){
    console.log('C');
    $felipePara.toggleClass('animated bounceOutDown');
    }
);
$pouyeshPic.click(function(){
    console.log('C');
    $pouyeshPara.toggleClass('animated rotateOutUpLeft');
    }
);


// $btn.hover(function() {
//     $btn.fadeOut( 100 );
//     $btn.fadeIn( 500 );
//   });

