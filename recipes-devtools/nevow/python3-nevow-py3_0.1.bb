SUMMARY = "Web Application Construction Kit"
HOMEPAGE = "https://github.com/beremiz/nevow-py3"
LICENSE = "CLOSED"

LIC_FILES_CHKSUM = "file://LICENSE;md5=50ad7cdebd8c5f7f1362c4adb8856265"

SRC_URI = "https://github.com/beremiz/nevow-py3.git"
SRC_URI[sha256sum] = "3b1a0cdada1d47b896cfb3f5ee27aae5fd7a3896c6feb69c8406802cac9f2a86"

SRCREV = "${AUTOREV}"

S = "${WORKDIR}"

RDEPENDS_${PN} = " \
         ${PYTHON_PN}-twisted \      
"

inherit python3targetconfig 




