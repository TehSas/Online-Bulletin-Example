### ONLINE BULLETIN SCREEN ###

transform loading_dot1a:
    yoffset 0
    pause 0.25
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform loading_dot2a:
    yoffset 0
    pause 0.5
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform loading_dot3a:
    yoffset 0
    pause 0.75
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform news_fade:
    on idle:
        alpha 1.0
        linear 0.15 alpha 0.75
    on hover:
        alpha 0.75
        linear 0.15 alpha 1.0
transform loading_start_:
    on show:
        alpha 1.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0
transform loading_trans_:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

screen show_bulletin:
    zorder 100
    modal True
    default load_screen_bullet = True
    add "#000000" alpha 0.9
    if selected_bullet2['img2'] == '' or len(selected_bullet2["text"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_bulletin")]

    else:
        frame:
            xalign 0.5
            yalign 0.5
            background None

            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            vbox:
                text selected_bullet2['title'] color "#FFFFFF" text_align 0.5 xalign 0.5
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 40
                imagebutton:
                    xalign 0.5
                    idle fetch_image(selected_bullet2['img2'])#NewsImage
                    action NullAction()

                vbox:
                    for i in selected_bullet2["text"]:
                        text i['text'] color "#FFFFFF" xsize 1500 text_align 0.5

        imagebutton:
            idle Text("{color=#808080}CLOSE", size = 75, bold=True)
            hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True)
            xalign 0.5
            yalign 1.0
            yoffset -50
            action [SetVariable("bullet_screen",False),Hide("show_bulletin")]

default selected_nl = None
default nl_screen = False
default nl_delay = False
screen show_newsletter:
    zorder 100
    modal True
    default load_screen_bullet = True
    add "#000000" alpha 0.9
    #text str(len(loaded_img_cache))
    if selected_bullet2["title"] == '' or len(selected_bullet2["imgs"]) == 0 or len(selected_bullet2["desc"]) == 0 or len(selected_bullet2["bulls"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),SetVariable("selected_nl",None),Hide("show_newsletter")]

    else:
        if selected_bullet['id'] not in loaded_img_cache:
            timer 0.01 action Show("newsletter_image_load")

        if selected_nl != None:
            frame:
                xalign 0.0
                yalign 0.5
                background None

                add Transform(Solid("#000000", xysize=(2000, 850),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                viewport at loading_trans_:
                    xysize (2000, 750)
                    mousewheel True
                    xalign 0.0
                    yalign 0.5
                    xoffset 1225
                    yoffset -20
                    vbox:
                        xalign 0.0
                        yalign 0.5
                        #spacing 40
                        text selected_bullet2['title'] color "#FFFFFF" size 40 text_align 0.5 bold True

                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        for i in selected_bullet2["desc"]:
                            text i['nl_text'] color "#FFFFFF" size 25 text_align 0.5 bold False xsize 700

                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True
                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        for i in selected_bullet2["bulls"]:
                            vbox:
                                spacing 25
                                text i['title'] color "#FFFFFF" size 30 bold True xsize 600
                                for ii in i["texts"]:
                                    text ii['nl_text'] color "#FFFFFF" size 20 bold False xsize 600
                                text "" color "#FFFFFF" size 20 text_align 0.5 bold True


                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 40
                    #text selected_bullet['title'] color "#FFFFFF" xsize 1500 text_align 0.5 bold True
                    for i in selected_bullet2["imgs"]:
                        if i == selected_nl:
                            #text i['text_top'] color "#FFFFFF" xsize 1500 text_align 0.5
                            imagebutton:
                                xalign 0.0
                                yalign 0.5
                                idle Transform(fetch_image(i['nl_img']),zoom=0.5)#NewsImage
                                action NullAction()
                            #text i['text_bottom'] color "#FFFFFF" xsize 1500 text_align 0.5

                    hbox:
                        xalign 0.0
                        yalign 0.5
                        xoffset 10
                        yoffset -65
                        spacing 10
                        if selected_bullet2["imgs"].index(selected_nl) == 0:
                            textbutton _("<") action [SetVariable("selected_nl",selected_bullet2["imgs"][-1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 55
                        else:
                            textbutton _("<") action [SetVariable("selected_nl",selected_bullet2["imgs"][selected_bullet2["imgs"].index(selected_nl)-1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" ysize 75 yoffset 55


                        for i in selected_bullet2["imgs"]:
                            if selected_nl == i:
                                textbutton _(".") action [NullAction(),SetVariable("nl_delay",True)] text_size 200 text_idle_color "#FFFFFF" text_hover_color "#FFFFFF" ysize 75
                            else:
                                textbutton _(".") action [SetVariable("selected_nl",i),SetVariable("nl_delay",True)] text_size 200 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75

                        if selected_bullet2["imgs"].index(selected_nl) == len(selected_bullet2["imgs"])-1:
                            textbutton _(">") action [SetVariable("selected_nl",selected_bullet2["imgs"][0]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 55
                        else:
                            textbutton _(">") action [SetVariable("selected_nl",selected_bullet2["imgs"][selected_bullet2["imgs"].index(selected_nl)+1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 55

            imagebutton:
                idle Text("{color=#808080}CLOSE", size = 50, bold=True)
                hover Text("{color=#FFFFFF}CLOSE", size = 50, bold=True)
                xalign 0.5
                yalign 1.0
                yoffset -15
                action [SetVariable("bullet_screen",False),SetVariable("selected_nl",selected_bullet2["imgs"][0]),Hide("show_newsletter")]
screen newsletter_image_load:
    zorder 999
    modal True
    default loading_images = False
    default load_go = False
    add "#000000" alpha 0.9
    add Text("LOADING IMAGES", size=25, color="#FFFFFF", bold=True) xalign 0.5 yalign 0.5 yoffset 150
    hbox:
        xalign 0.5 yalign 0.5
        spacing 50
        add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot1a
        add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot2a
        add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot3a


    if loading_images == False:
        timer 0.5 action SetScreenVariable("load_go",True)

    if load_go == True:
        for a in selected_bullet2['imgs']:
            $ batch_fetch_images(a['nl_img'])

    timer 1.0 action [SetVariable("selected_nl",selected_bullet2["imgs"][0]),Hide("newsletter_image_load")]

screen show_list:
    zorder 100
    modal True
    add "#000000" alpha 0.9

    #$ active_patrons = []
    #for a in selected_bullet2["tiers"]:
        ##if a['active'] == "True" and a['id'] in persistent.branch_check:
        #$ active_patrons.append(a)

    if len(selected_bullet2["listing"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_list")]
    else:
        frame:
            xalign 0.5
            yalign 0.5
            background None
            add Transform(Solid("#FFFFFF", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            viewport at loading_trans_:
                xysize (1700, 750)#xysize (1890, 750)
                mousewheel True
                xalign 0.5
                yalign 0.5
                add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            viewport at loading_trans_:
                xysize (1700, 750)#xysize (1890, 750)
                mousewheel True
                xalign 0.5
                yalign 0.5
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 5
                    for i in selected_bullet2['listing']:
                        frame:
                            background None
                            xsize 1700
                            ysize 150
                            hbox:
                                add Transform(fetch_image(i['icon']),zoom=0.5)
                                vbox:
                                    text i['title'] color "#FFFFFF" size 45 yoffset -5
                                    text i['desc'] size 25 color "#8C8C8C" yoffset 25
                                if i['button'] == '':
                                    pass
                                else:
                                    text " - " yoffset 10
                                    textbutton i['button'] text_idle_color "#FFFFFF" text_hover_color i["color"] text_size 45 yoffset -5 action OpenURL(i["link"])


        imagebutton:
            idle Text("{color=#808080}CLOSE", size = 75, bold=True)
            hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True)
            xalign 0.5
            yalign 1.0
            yoffset -50
            action [SetVariable("bullet_screen",False),Hide("show_list")]

default selected_bullet = None
default selected_bullet2 = None
default bullet_screen = False
default bullet_delay = False
screen bulletin_board:
    timer 0.01 action Function(update_news)

    $ active_bulletins = []
    if persistent.news != None:
        for a in persistent.current_news['main_bulletin']:
            if a['active'] == "True" and a['id'] in persistent.branch_check:
                $ active_bulletins.append(a)

    viewport at loading_trans_:
        xysize (750, 175)
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15
        add "#000000c0" alpha 0.75
        add "#FFFFFF" alpha 0.5
    viewport at loading_trans_:
        xysize (750, 175)
        mousewheel True
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15

        vbox:
            frame:
                background None
                ysize 5
                text ""
            if persistent.current_news == None:
                text "OFFLINE" size 75 color "#808080" bold False xoffset 200 yoffset 40
            else:
                if persistent.current_news['maintenance'] == 'True':
                    text "* Maintenance Being Done *" size 50 color "#808080" bold False xoffset 10 yoffset 55
                else:
                    if len(active_bulletins) == 0:
                        text "* Maintenance Being Done *" size 50 color "#808080" bold False xoffset 10 yoffset 55
                    else:
                        timer 0.01 action SetVariable("selected_bullet",active_bulletins[0])
                        if selected_bullet != None:
                            imagebutton:
                                idle fetch_image(selected_bullet['img'])
                                yoffset -5
                                if selected_bullet['bull_type'] == "screen_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_bulletin")]
                                elif selected_bullet['bull_type'] == "web_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),OpenURL(selected_bullet["link"])]
                                elif selected_bullet['bull_type'] == "newsletter_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_newsletter")]
                                elif selected_bullet['bull_type'] == "list_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_list")]
                                else:
                                    action NullAction()

    if bullet_delay != False:
        timer 0.25 action SetVariable("bullet_delay",False)

    if persistent.current_news == None:
        hbox:
            xalign 0.5
            xoffset 550
            yoffset 150
            spacing 25
            textbutton _("<") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" ysize 75 yoffset 25

            textbutton _(".") action NullAction() text_size 100 text_idle_color "#757575" text_hover_color "#757575" ysize 75

            textbutton _(">") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" ysize 75 yoffset 25
    else:
        if persistent.current_news['maintenance'] == 'True' or len(active_bulletins) == 0:
            hbox:
                xalign 0.5
                xoffset 550
                yoffset 150
                spacing 25
                textbutton _("<") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" ysize 75 yoffset 25

                textbutton _(".") action NullAction() text_size 100 text_idle_color "#757575" text_hover_color "#757575" ysize 75

                textbutton _(">") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" ysize 75 yoffset 25
        else:
            if selected_bullet != None:
                if bullet_screen == False:
                    if active_bulletins.index(selected_bullet) == len(active_bulletins)-1:
                        if bullet_delay == False:
                            timer 5.0 repeat True action SetVariable("selected_bullet",active_bulletins[0])
                    else:
                        if bullet_delay == False:
                            timer 5.0 repeat True action SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)+1])

                hbox:
                    xalign 0.5
                    xoffset 550
                    yoffset 150
                    spacing 25
                    if active_bulletins.index(selected_bullet) == 0:
                        textbutton _("<") action [SetVariable("selected_bullet",active_bulletins[-1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 25
                    else:
                        textbutton _("<") action [SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)-1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 25


                    for i in active_bulletins:
                        if selected_bullet == i:
                            textbutton _(".") action [NullAction(),SetVariable("bullet_delay",True)] text_size 100 text_idle_color "#FFFFFF" text_hover_color "#FFFFFF" ysize 75
                        else:
                            textbutton _(".") action [SetVariable("selected_bullet",i),SetVariable("bullet_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75

                    if active_bulletins.index(selected_bullet) == len(active_bulletins)-1:
                        textbutton _(">") action [SetVariable("selected_bullet",active_bulletins[0]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 25
                    else:
                        textbutton _(">") action [SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)+1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" ysize 75 yoffset 25









label quit:
    $ persistent.news = None
    $ persistent.current_news = None
    $ cleanup_temp_files()
