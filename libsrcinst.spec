%define shortname srcinst

%define major 0
%define libname %mklibname %{shortname} %{major}
%define devname %mklibname %{shortname} -d

Summary:	Basic library used by sourceinstall
Name:		libsrcinst
Version:	2.5
Release:	5
License:	GPLv3+
Group:		System/Libraries
Url:		http://www.gnu.org/software/sourceinstall
Source0:	ftp://ftp.gnu.org/gnu/sourceinstall/%{name}-%{version}.tar.gz
BuildRequires:	install-info

%description
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Basic library used by sourceinstall
Group:		System/Libraries

%description -n %{libname}
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development headers for the sourceinstall library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Libsrcinst is the basic library used by the sourceinstall application.
Sourceinstall provides a way to centralize source installation.

%files -n %{devname} -f %{name}.lang
%doc AUTHORS README.API TODO
%{_includedir}/%{shortname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
PATH=$PATH:/sbin %configure2_5x --disable-static
%make

%install
PATH=$PATH:/sbin %makeinstall_std

%find_lang %{name}

