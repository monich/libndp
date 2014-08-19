Name: libndp
Version: 1.4
Release: 0
Summary: Library for Neighbor Discovery Protocol
Group: Development/Libraries
License: GPLv2
URL: https://github.com/jpirko/libndp
Source: %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Library for Neighbor Discovery Protocol

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the development library for %{name}.

%package tools
Summary: Neighbor Discovery Protocol tools
Requires: %{name} = %{version}

%description tools
This package contains Neighbor Discovery Protocol tools

%prep
%setup -q -n %{name}-%{version}/libndp

%build
./autogen.sh
./configure --prefix=%{_prefix}
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.a
rm %{buildroot}%{_libdir}/*.la
rm -fr %{buildroot}%{_mandir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig

%files tools
%defattr(-,root,root,-)
%{_bindir}/ndptool
