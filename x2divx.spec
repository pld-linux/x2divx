Summary:	AVI && MPEG to DivX AVI converter
Summary(pl):	Konwerter AVI i MPEG do DivX AVI
Name:		x2divx
Version:	0.8
Release:	1
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
Source0:	http://www.emulinks.de/divx/%{name}-%{version}.tar.gz
URL:		http://www.emulinks.de/divx/
BuildRequires:	avifile-devel >= 0.6
BuildRequires:	libmpeg3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for converting AVI and MPEG to DivX encoded AVIs.

%description -l pl
Narzêdzie do konwertowania plików AVI i MPEG do AVI kompresowanych
DivXem.

%prep
%setup  -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -funroll-loops -o avi2divx avi2divx.cpp \
		-I/usr/X11R6/include/avifile -L/usr/X11R6/lib \
		-laviplay -lpthread
%{__cc} %{rpmcflags} %{rpmldflags} -funroll-loops -o mpeg2divx mpeg2divx.cpp \
		-I/usr/X11R6/include/avifile -L/usr/X11R6/lib \
		-laviplay -lpthread -lmpeg3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install avi2divx	$RPM_BUILD_ROOT%{_bindir}
install	mpeg2divx	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
