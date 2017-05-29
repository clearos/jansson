Name:       jansson
Version:    2.5
Release:    1%{?dist}
Summary:    C library for encoding, decoding and manipulating JSON data

Group:      System Environment/Libraries
License:    MIT
URL:        http://www.digip.org/jansson/
Source0:    http://www.digip.org/jansson/releases/jansson-%{version}.tar.bz2

BuildRequires:  python-sphinx
BuildRequires: libtool

%description
Small library for parsing and writing JSON documents.

%package devel
Summary: Header files for jansson
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Header files for developing applications making use of jansson.

%package devel-doc
Summary: Development documentation for jansson

%description devel-doc
Development documentation for jansson.

%prep
%setup -q
autoreconf -i

%build
%configure --disable-static
make %{?_smp_mflags}
make html

%check
make check

%install
make install INSTALL="install -p" DESTDIR="$RPM_BUILD_ROOT"
rm "$RPM_BUILD_ROOT%{_libdir}"/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE CHANGES
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files devel-doc
%doc doc/_build/html/*

%changelog
* Mon May 29 2017 ClearFoundation <developer@clearfoundation.com> 2.5-1
- Merged specs from EPEL and other sources
