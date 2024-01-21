#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Beremiz, a Integrated Development Environment for
# programming IEC 61131-3 automates supporting plcopen standard and CanFestival.
#
# Copyright (C) 2016: Andrey Skvortsov
#
# See COPYING file for copyrights details.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.






import os

def GetCommunityHelpMsg():
    return _(
        "The best place to ask questions about Beremiz/PLCOpenEditor\n"
        "is project's mailing list: beremiz-devel@lists.sourceforge.net\n"
        "\n"
        "This is the main community support channel.\n"
        "For posting it is required to be subscribed to the mailing list.\n"
        "\n"
        "You can subscribe to the list here:\n"
        "https://lists.sourceforge.net/lists/listinfo/beremiz-devel"
    )


def GetAboutDialogInfo(info):

    info.Version = app_version

    info.Copyright = ""
    info.Copyright += "(C) 2006-2023 Edouard Tisserant\n"
    info.Copyright += "(C) 2003-2023 Mario de Sousa\n"
    info.Copyright += "(C) 2022-2023 GP Orcullo\n"
    info.Copyright += "(C) 2016-2018 Andrey Skvortsov\n"
    info.Copyright += "(C) 2006-2013 Laurent Bessard\n"

    info.WebSite = ("http://beremiz.org", "beremiz.org")

    info.Developers = (
        "Edouard Tisserant <contact@beremiz.fr>",
        "Mario de Sousa <msousa@fe.up.pt>",
        "GP Orcullo <kinsamanka@gmail.com>",
        "Andrey Skvortsov <andrej.skvortzov@gmail.com>",
        "Sergey Surkov <surkov.sv@summatechnology.ru>",
        "Laurent Bessard <laurent.bessard@gmail.com>")

    info.License = (
        '\n This program is free software; you can redistribute it and/or\n'
        ' modify it under the terms of the GNU General Public License\n'
        ' as published by the Free Software Foundation; either version 2\n'
        ' of the License, or (at your option) any later version.\n'
        '\n'
        ' This program is distributed in the hope that it will be useful,\n'
        ' but WITHOUT ANY WARRANTY; without even the implied warranty of\n'
        ' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n'
        ' GNU General Public License below for more details.\n'
        '\n'
        '\n'
        '\n'
        ''
    )

    # read license file
    license_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "COPYING")
    if os.path.exists(license_path):
        with open(license_path) as f:
            info.License += f.read()

    info.Translators = (
        "Basque",
        "José Miguel Andonegi <jm.andonegi@gmail.com>, 2019",
        "",

        "Bengali (Bangladesh)",
        "  Adhir Dutta <likhon52@gmail.com>, 2017",
        "",

        "Chinese",
        "  Frank Guan <gpfrank@163.com>, 2018",
        "  Tango Wu <wuyangtang@live.com>, 2017",
        "  Yiwei Yan <523136664@qq.com>, 2018",
        "  Ji Wang <2485567515@qq.com>, 2019",
        "  珂 曾 <15627997@qq.com>, 2019",
        "  Gastonfeng<gastonfeng@gmail.com>, 2019",
        "",

        "Dutch (Netherlands)",
        "  Martijn Berntsen <mxberntsen@gmail.com>, 2019",
        "  Jordy van der Heijden <jordyvanderheijden@gmail.com>, 2018",
        "",

        "French",
        "  Edouard Tisserant <edouard.tisserant@gmail.com>, 2018",
        "  Fabien Marteau <mail@fabienm.eu>, 2017",
        "  Laurent Bessard <laurent.bessard@gmail.com>, 2008",
        "",

        "German",
        "  Andrey Skvortsov <andrej.skvortzov@gmail.com>, 2017",
        "  Hendrik Knackstedt <h.knackstedt@stud.uni-hannover.de>, 2017 ",
        "  Mark Muzenhardt <mark.muzenhardt@gmail.com>, 2012",
        "",

        "Hungarian",
        "  Krisztián Veress <krive001@gmail.com>, 2018",
        "  Gábor Véninger <veninger.gabor@gmail.com>, 2017",
        "",

        "Italian",
        "  Luca Magnabosco <magnabosco.luca@gmail.com>, 2017",
        "  Manuele Conti <manuele.conti@sirius-es.it>, 2017",
        "",

        "Korean",
        "  Ikhwan Kim <duo821228@gmail.com>, 2018",
        "  Reinhard Lee <lij3105@gmail.com>, 2012",
        "",

        "Polish",
        "  Adam B <adisz.pl@gmail.com>, 2019",
        "",

        "Portuguese",
        "  Pedro Coimbra <pcoimbra310@gmail.com>, 2017",
        "",

        "Portuguese (Brazil)",
        "  Rodrigo Rolle <ro_pita@hotmail.com>, 2018",
        "  Thiago Alves <thiagoralves@gmail.com>, 2017",
        "",

        "Romanian",
        "  Emil Saracutu <emil_saracutu@yahoo.com>, 2018",
        "",

        "Russian",
        "  Andrey Skvortsov <andrej.skvortzov@gmail.com>, 2018",
        "  Sergey Surkov <surkov.sv@summatechnology.ru>, 2018",
        "  zx_alexis <zxalexis@gmail.com>, 2017",
        "",

        "Slovenian",
        "  Janez Pregelj <janezpregelj@gmail.com>, 2018",
        "  Andraz Gregorcic <andraz.gregorcic@smarteh.si>, 2017",
        "",

        "Spanish",
        "  Carlos Guilarte <guilartec@gmail.com>, 2018",
        "  Yegor Yefremov <yegorslists@googlemail.com>, 2018",
        "  Jorge Rojas, 2018",
        "  Marcial González de Armas <mgacod@gmail.com>, 2017",
        "  Nelson Mambre <nmambre@gmail.com>, 2017",
        "",

        "Turkish",
        "  Ibrahim Kilicarslan <ibrahimhalilkilicarslan@outlook.com>, 2018",
        "",

        "Vietnamese (Viet Nam)",
        "  Nhất Thìn, 2019",
        "",


    )
    return info


app_version = "1.4-beta2"

if __name__ == "__main__":
    print(app_version)
