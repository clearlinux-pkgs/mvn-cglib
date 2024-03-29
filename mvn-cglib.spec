#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-cglib
Version  : elease.3.2.0
Release  : 7
URL      : https://github.com/cglib/cglib/archive/RELEASE_3_2_0.tar.gz
Source0  : https://github.com/cglib/cglib/archive/RELEASE_3_2_0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.jar
Source2  : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.pom
Source3  : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.jar
Source4  : https://repo.maven.apache.org/maven2/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.pom
Source5  : https://repo.maven.apache.org/maven2/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom
Source6  : https://repo1.maven.org/maven2/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.jar
Source7  : https://repo1.maven.org/maven2/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.pom
Source8  : https://repo1.maven.org/maven2/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom
Source9  : https://repo1.maven.org/maven2/cglib/cglib-parent/3.2.5/cglib-parent-3.2.5.pom
Source10  : https://repo1.maven.org/maven2/cglib/cglib-parent/3.2.9/cglib-parent-3.2.9.pom
Source11  : https://repo1.maven.org/maven2/cglib/cglib/3.1/cglib-3.1.jar
Source12  : https://repo1.maven.org/maven2/cglib/cglib/3.1/cglib-3.1.pom
Source13  : https://repo1.maven.org/maven2/cglib/cglib/3.2.0/cglib-3.2.0.jar
Source14  : https://repo1.maven.org/maven2/cglib/cglib/3.2.0/cglib-3.2.0.pom
Source15  : https://repo1.maven.org/maven2/cglib/cglib/3.2.5/cglib-3.2.5.jar
Source16  : https://repo1.maven.org/maven2/cglib/cglib/3.2.5/cglib-3.2.5.pom
Source17  : https://repo1.maven.org/maven2/cglib/cglib/3.2.9/cglib-3.2.9.jar
Source18  : https://repo1.maven.org/maven2/cglib/cglib/3.2.9/cglib-3.2.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1 Apache-2.0
Requires: mvn-cglib-data = %{version}-%{release}
Requires: mvn-cglib-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
cglib [![Build Status](https://travis-ci.org/cglib/cglib.svg?branch=master)](https://travis-ci.org/cglib/cglib)
================

%package data
Summary: data components for the mvn-cglib package.
Group: Data

%description data
data components for the mvn-cglib package.


%package license
Summary: license components for the mvn-cglib package.
Group: Default

%description license
license components for the mvn-cglib package.


%prep
%setup -q -n cglib-RELEASE_3_2_0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-cglib
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-cglib/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-cglib/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.5/cglib-parent-3.2.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.9
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.9/cglib-parent-3.2.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.1
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.1/cglib-3.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.1/cglib-3.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.0/cglib-3.2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.0/cglib-3.2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.5
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.5/cglib-3.2.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.5
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.5/cglib-3.2.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.9
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.9/cglib-3.2.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.9
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/cglib/cglib/3.2.9/cglib-3.2.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.jar
/usr/share/java/.m2/repository/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.pom
/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.jar
/usr/share/java/.m2/repository/cglib/cglib-nodep/2.2.2/cglib-nodep-2.2.2.pom
/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.jar
/usr/share/java/.m2/repository/cglib/cglib-nodep/3.2.9/cglib-nodep-3.2.9.pom
/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.0/cglib-parent-3.2.0.pom
/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.5/cglib-parent-3.2.5.pom
/usr/share/java/.m2/repository/cglib/cglib-parent/3.2.9/cglib-parent-3.2.9.pom
/usr/share/java/.m2/repository/cglib/cglib/3.1/cglib-3.1.jar
/usr/share/java/.m2/repository/cglib/cglib/3.1/cglib-3.1.pom
/usr/share/java/.m2/repository/cglib/cglib/3.2.0/cglib-3.2.0.jar
/usr/share/java/.m2/repository/cglib/cglib/3.2.0/cglib-3.2.0.pom
/usr/share/java/.m2/repository/cglib/cglib/3.2.5/cglib-3.2.5.jar
/usr/share/java/.m2/repository/cglib/cglib/3.2.5/cglib-3.2.5.pom
/usr/share/java/.m2/repository/cglib/cglib/3.2.9/cglib-3.2.9.jar
/usr/share/java/.m2/repository/cglib/cglib/3.2.9/cglib-3.2.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-cglib/LICENSE
/usr/share/package-licenses/mvn-cglib/NOTICE
