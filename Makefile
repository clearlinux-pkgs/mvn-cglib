PKG_NAME := mvn-cglib
URL = https://github.com/cglib/cglib/archive/RELEASE_3_2_0.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/cglib/cglib/3.2.0/cglib-3.2.0.jar : https://repo1.maven.org/maven2/cglib/cglib/3.2.0/cglib-3.2.0.pom : https://repo.maven.apache.org/maven2/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.pom : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.jar : 

include ../common/Makefile.common
