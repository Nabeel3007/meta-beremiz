SUMMARY = "Serialization based on ast.literal_eval"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE;md5=d7c28f460fafe7be454fcdcac0b60263"

SRC_URI[md5sum] = "c0ddaba7d2625631968bec8553ab95b1"
SRC_URI[sha256sum] = "0407035fe3c6644387d48cff1467d5aa9feff814d07372b78677ed0ee3ed7095"

inherit pypi setuptools3

SRC_URI += " \
    file://run-ptest \
"

RDEPENDS:${PN}-ptest += " \
"

do_install_ptest() {
    install -d ${D}${PTEST_PATH}/tests
    cp -rf ${S}/tests/* ${D}${PTEST_PATH}/tests/
}

RDEPENDS:${PN} += "\
    ${PYTHON_PN}-netclient \
    ${PYTHON_PN}-numbers \
"    
