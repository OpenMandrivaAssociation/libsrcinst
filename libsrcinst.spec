%define shortname	srcinst

%define major		0
%define libname		%mklibname %{shortname} %{major}
%define develname	%mklibname %{shortname} -d

Summary:	Basic library used by sourceinstall
Name:		libsrcinst
Version:	2.5
Release:	%{mkrel 3}
License:	GPLv3+
Group:		System/Libraries
Source0:	ftp://ftp.gnu.org/gnu/sourceinstall/%{name}-2.5.tar.gz
URL:		http://www.gnu.org/software/sourceinstall
Buildroot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	info-install
BuildRequires:	zip 
BuildRequires:	unzip 
BuildRequires:	bzip2 
BuildRequires:	ncompress 
BuildRequires:	gzip 
BuildRequires:	tar

%description
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

%package -n %{libname}
Summary:	Basic library used by sourceinstall
Group:		System/Libraries
Obsoletes:	%{libname} < %{libname}-%{version}

%description -n %{libname}
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

%package -n %{develname}
Summary:	Development headers for the sourceinstall library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

%prep
%setup -q

%build
PATH=$PATH:/sbin %configure2_5x
%make

%install
PATH=$PATH:/sbin %makeinstall_std
%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname} -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README.API TODO
%{_includedir}/%{shortname}
%{_libdir}/%{name}.*a
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/*/*


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.5-3mdv2010.0
+ Revision: 439445
- rebuild

* Thu Nov 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.5-2mdv2009.1
+ Revision: 300349
- add buildrequires for the various compression tools

* Thu Nov 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.5-1mdv2009.1
+ Revision: 300292
- import libsrcinst


