Summary:	AVI && MPEG to DivX AVI converter
Summary(pl):	Konwerter AVI i MPEG do DivX AVI
Name:		x2divx
Version:	0.10a
Release:	2
Group:		X11/Applications/Multimedia
License:	GPL
Source0:	http://www.emulinks.de/divx/%{name}-%{version}.tar.gz
# Source0-md5:	07a46bc1b9e6869900956db4adec866f
URL:		http://www.emulinks.de/divx/
BuildRequires:	avifile-devel >= 1:0.6
BuildRequires:	libmpeg3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _CFLAGS -O3 -funroll-loops
%define _LIBS	-L/usr/lib -laviplay -lpthread
%define _INC	-I/usr/include/libmpeg3 -I/usr/include/avifile -I/usr/include

%description
Tools for converting AVI and MPEG to DivX encoded AVIs.

%description -l pl
Narzêdzie do konwertowania plików AVI i MPEG do AVI kompresowanych
DivXem.

%prep
%setup -q

%build

%{__cxx} %{rpmcflags} %{rpmldflags} %{_CFLAGS} %{_INC} %{_LIBS} -o avi2divx avi2divx.cpp
%{__cxx} %{rpmcflags} %{rpmldflags} %{_CFLAGS} %{_INC} %{_LIBS} -o mpeg2divx mpeg2divx.cpp -lmpeg3



%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install avi2divx	$RPM_BUILD_ROOT%{_bindir}
install	mpeg2divx	$RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc ChangeLog NEWS README README.jpc TODO
