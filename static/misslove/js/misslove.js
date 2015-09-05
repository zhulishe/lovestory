/**
 * Created by donald on 15-9-4.
 */
$(document).ready(function() {

    /**************基础页面(base.html)******************/
	$('.to-top').toTop({
        right: 30,
        bottom: 70,
        offset: 300
    });
    $("#messages").delay(2000).hide("slow");

    tinymce.init({
        selector: "textarea",
        language: "zh_CN",
        toolbar: "insertfile undo redo | styleselect | fontsizeselect bold italic | alignleft aligncenter" +
            " alignright alignjustify | bullist numlist outdent indent ",

    });

     $(function () {
        $('[data-toggle="tooltip"]').tooltip()
        });


    /*************首页(homepage.html)*****************/
    $(".carousel").carousel({interval: 3000}).carousel('cycle');
    $("#hp-container > div > div").hover(function(){
        $(this).addClass(function(){
            return 'div-hover-'+$(this).parent().index()
        }).find("img").removeClass("gray")
            .parent().find("p").addClass(function(){
                return 'p-hover-'+$(this).parent().parent().index()
            });},
        function(){
            $(this).removeClass(function(){
                return 'div-hover-'+$(this).parent().index()
            }).find("img").addClass("gray")
                .parent().find("p").removeClass(function(){
                    return 'p-hover-'+$(this).parent().parent().index()
                });
        });


    /*************新建文章(new_article.html)*******************/
    $(".article-edit").find("#id_title").prev().text("标题: ");
    $(".article-edit").find("#id_title").next().text("文章内容: ");
    $(".article-edit").find("#id_choose_type").prev().text("板块类型: ");
    $(".article-edit").find("input").addClass("form-control");
    $(".article-edit").find("select").addClass("form-control");


    /**************修改评论(edit_comment.html)********************/
    $(".comment-edit label").text("评论内容：");



});

