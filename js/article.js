window.onload = function(){
    $(function(){
        $("#header").load("../html/header.html",function() {
        var imgs = document.images,
        len = imgs.length,
        counter = 0;

        [].forEach.call( imgs, function( img ) {
            if(img.complete)
            incrementCounter();
            else
            img.addEventListener( 'load', incrementCounter, false );
        } );

        function incrementCounter() {
            counter++;
            if ( counter === len ) {
                let toggle = document.querySelector("#header .toggle-button");
                let collapse = document.querySelectorAll("#header .collapse");
                toggle.addEventListener('click' , function(){
                    collapse.forEach(col => col.classList.toggle("collapse-toggle"));
                })
                new Masonry("#posts .grid", {
                    itemSelector : '.grid-item',
                    gutter : 20
                });
                new Swiper('.swiper-container', {
                    direction : 'horizontal',
                    loop : true,
                    slidesPerView : 5,
                    autoplay : {
                        delay : 3000
                    },
                    breakpoints : {
                        '@0' : {
                            slidesPerView : 2
                        },
                        '@1.00' : {
                            slidesPerView : 3
                        },
                        '@1.25' : {
                            slidesPerView : 4
                        },
                        '@1.50' : {
                            slidesPerView: 5
                        }
                    }
                })
                window.onscroll = function(){ myFunction()};
                let navbar = document.getElementById("header");
                let sticky = navbar.offsetTop;
                function myFunction(){
                    if(window.pageYOffset >= sticky){
                        navbar.classList.add("sticky");
                    }else{
                        navbar.classList.remove("sticky");
                    }
                }
                $("#footer").load("../html/footer.html"); 
            }
        }


        });
    });
}