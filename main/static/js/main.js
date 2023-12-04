$(document).ready(function(){

    var checkClosed = function(item){
        $.cookie.json = true;
        var arClosed = $.cookie("MSHOP_FILTER_CLOSED");
        if (arClosed && typeof arClosed != "undefined"){
            if (typeof item != "undefined"){
                var propID = item.parents(".bx_filter_parameters_box").data("property_id");
                var delIndex = $.inArray(propID, arClosed);
                if (delIndex >= 0) { arClosed.splice(delIndex,1);} else {arClosed.push(propID);}
            }
        }else{
            var arClosed = [];
            if (typeof item != "undefined"){
                item = $(item);
                var propID = item.parents(".bx_filter_parameters_box").data("property_id");
                if (!item.parents(".bx_filter_parameters_box").is(".active")) { if (!$.inArray(propID, arClosed) >= 0) { arClosed.push(propID); } }
                else { if ($.inArray(propID, arClosed) >= 0) { arClosed.splice(delIndex,1); } }
            }
        }
        $.cookie("MSHOP_FILTER_CLOSED", arClosed, {
            path: '/',
            domain: '',
            expires: 360
        });
        return true;
    }
    var checkOpened = function(item){
        $.cookie.json = true;
        var arOpened = $.cookie("KSHOP_FILTER_OPENED");
        if (arOpened && typeof arOpened != "undefined"){
            if (typeof item != "undefined"){
                var propID = item.parents(".bx_filter_parameters_box").data("property_id");
                var delIndex = $.inArray(propID, arOpened);
                if (delIndex >= 0) { arOpened.splice(delIndex,1); checkClosed(item); }
                else { arOpened.push(propID); checkClosed(item); }
            }else{
                $(".bx_filter_parameters_box").each(function(){
                    var propID = $(this).data("property_id");
                    if ($(this).is(".active")) { if ($.inArray(propID, arOpened) < 0) { arOpened.push(propID); checkClosed(item); } }
                });
            }
        }else{
            var arOpened = [];
            if (typeof item != "undefined"){
                item = $(item);
                var propID = item.parents(".bx_filter_parameters_box").data("property_id");
                if (item.parents(".bx_filter_parameters_box").is(".active")) { if (!$.inArray(propID, arOpened) >= 0) { arOpened.push(propID); checkClosed(item); }  }
                else { if ($.inArray(propID, arOpened) >= 0) { arOpened.splice(delIndex,1); checkClosed(item); } }
            }else{
                $(".bx_filter_parameters_box").each(function()
                {
                    var propID = $(this).data("property_id");
                    if ($(this).is(".active")) { if ($.inArray(propID, arOpened) < 0) { arOpened.push(propID); checkClosed(item); } }
                });
            }
        }
        $.cookie("MSHOP_FILTER_OPENED", arOpened,{
            path: '/',
            domain: '',
            expires: 360
        });
        return true;
    }
    //checkOpened();
    $(".bx_filter_parameters_box_title").on('click',function(){
        var active=2;
        if ($(this).closest(".bx_filter_parameters_box").hasClass("active")) { $(this).next(".bx_filter_block").slideUp(100); }
        else { $(this).next(".bx_filter_block").slideDown(200); }
        $(this).closest(".bx_filter_parameters_box").toggleClass("active");

        if($(this).closest(".bx_filter_parameters_box").hasClass("active")){
            active=3;
        }
        //checkOpened($(this));

        $.cookie.json = true;
        $.cookie("MSHOP_filter_prop_"+$(this).closest(".bx_filter_parameters_box").data('prop_code'), active,{
            path: '/',
            domain: '',
            expires: 360
        });
    });
    $('.bx_filter_parameters_box').each(function(){
        if($.cookie("MSHOP_filter_prop_"+$(this).data('prop_code'))==2){
            $(this).removeClass('active');
            $(this).find('.bx_filter_block').hide();
        }else if($.cookie("MSHOP_filter_prop_"+$(this).data('prop_code'))==3){
            $(this).addClass('active');
            $(this).find('.bx_filter_block').show();
        }
    })
    $(".hint .icon").on('click',function(e){
        var tooltipWrapp = $(this).parents(".hint");
        tooltipWrapp.click(function(e){e.stopPropagation();})
        if (tooltipWrapp.is(".active"))
        {
            tooltipWrapp.removeClass("active").find(".tooltip").slideUp(200);
        }
        else
        {
            tooltipWrapp.addClass("active").find(".tooltip").slideDown(200);
            tooltipWrapp.find(".tooltip_close").click(function(e) { e.stopPropagation(); tooltipWrapp.removeClass("active").find(".tooltip").slideUp(100);});
            $(document).click(function() { tooltipWrapp.removeClass("active").find(".tooltip").slideUp(100);});
        }
    });
    //$('label.sku').equalizeWidths();

    $(".internal_sections_list").ready(function(){
        $(".internal_sections_list .title .inner_block").click(function(){
            $(this).find('.hider').toggleClass("opened");
            $(this).closest(".internal_sections_list").find(".title").toggleClass('opened');
            $(this).closest(".internal_sections_list").find(".sections_list_wrapp").slideToggle(200);
            $.cookie.json = true;
            $.cookie("MSHOP_internal_sections_list_HIDE", $(this).find('.hider').hasClass("opened"),{path: '/',	domain: '',	expires: 360});
        });

        if($.cookie("MSHOP_internal_sections_list_HIDE") == 'false'){
            $(".internal_sections_list .title").removeClass("opened");
            $(".internal_sections_list .title .hider").removeClass("opened");
            $(".internal_sections_list .sections_list_wrapp").hide();
        }

        $('.left_block .internal_sections_list li.item > a.parent').on('click',function(e) {
            e.preventDefault();
            console.log(12);
            $(this).parent().find('.child_container').slideToggle();
        });
    });

    var MShopSectionID = '12';
    $('.internal_sections_list .cur').removeClass('cur');
    $('*[data-id="'+ MShopSectionID + '"]').addClass('cur').parents('.child_container').parent().addClass('cur');
    $('*[data-id="'+ MShopSectionID + '"]').parent().find('.menu_title').addClass('cur');

    //Перенес логику ползунка в шаблон для того,
    //чтобы через представление передавать
    //туда максимальные и минимальные значения
    //по другому никак :(
        
    /*//ползунок

    $('#price').change(function () {
        var val = $(this).val();
        $('#slider_price').slider("values",0,val);
    });

    $('#price2').change( function() {
        var val2 = $(this).val();
        $('#slider_price').slider("values",1,val2);
    });

    $( "#slider_price" ).slider({
        range: true,
        //orientation: "vertical",
        min: '{{ cost_data.cost_of__min }}',
        step: 500,
        max: '{{ cost_data.cost_of__max }}',
        values: [ 0, 700 ],
        slide: function( event, ui ) {
            //$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
            $('#price').val(ui.values[0]);
            $('#price2').val(ui.values[1]);
        }
    });
    //$( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
    //" - $" + $( "#slider-range" ).slider( "values", 1 ) );
    $('#price').val($('#slider_price').slider("values",0));
    $('#price2').val($('#slider_price').slider("values",1));*/

    //Плюс/минус в всплывающей корзину
    $(document).on('click', '.counter_block .plus', function() {
        var parent = $(this).parents('.counter_block');
        var cnt = parent.find('.popup-count').val();
        cnt++;
        parent.find('.popup-count').val(cnt);
    });
    $(document).on('click', '.counter_block .minus', function() {
        var parent = $(this).parents('.counter_block');
        var cnt = parent.find('.popup-count').val();
        cnt--;
        if (cnt < 1) cnt = 1;
        parent.find('.popup-count').val(cnt);
    });

})