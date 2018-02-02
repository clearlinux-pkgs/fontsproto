#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fontsproto
Version  : 2.1.3
Release  : 10
URL      : http://xorg.freedesktop.org/releases/individual/proto/fontsproto-2.1.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/proto/fontsproto-2.1.3.tar.gz
Summary  : Fonts extension headers
Group    : Development/Tools
License  : MIT-Opengroup
Requires: fontsproto-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
X Fonts Extension
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the fontsproto package.
Group: Development
Provides: fontsproto-devel

%description dev
dev components for the fontsproto package.


%package dev32
Summary: dev32 components for the fontsproto package.
Group: Default

%description dev32
dev32 components for the fontsproto package.


%package doc
Summary: doc components for the fontsproto package.
Group: Documentation

%description doc
doc components for the fontsproto package.


%prep
%setup -q -n fontsproto-2.1.3
pushd ..
cp -a fontsproto-2.1.3 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/FS.h
/usr/include/X11/fonts/FSproto.h
/usr/include/X11/fonts/font.h
/usr/include/X11/fonts/fontproto.h
/usr/include/X11/fonts/fontstruct.h
/usr/include/X11/fonts/fsmasks.h
/usr/lib64/pkgconfig/fontsproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32fontsproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/fontsproto/*
