Summary:	DevHelp book: atk
Summary(pl):	Ksi±¿ka do DevHelp'a o atk
Name:		devhelp-book-atk
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/atk.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about atk

%description -l pl
Ksi±¿ka do DevHelp o atk

%prep
%setup -q -c atk -n atk

%build
mv -f book atk
mv -f book.devhelp atk.devhelp

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/atk
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install atk.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install atk/* $RPM_BUILD_ROOT%{_prefix}/books/atk

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs
