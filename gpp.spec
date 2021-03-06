Summary: Generic Preprocessor
%define packagename genpp
%define tarballname gpp
Name: %{packagename}
Version: 2.25-SNAPSHOT
Release: 2
License: LGPL
Group: Development/Languages/Other
URL: https://logological.org/gpp/
Source0: http://www.nothingisreal.com/gpp/%{tarballname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix: %{_prefix}

%description 
GPP is a general-purpose preprocessor with customizable syntax,
suitable for a wide range of preprocessing tasks. Its independence
from any one programming language makes it much more versatile than
the C preprocessor (cpp), while its syntax is lighter and more
flexible than that of GNU m4. There are built-in macros for use with
C/C++, LaTeX, HTML, XHTML, and Prolog files.

%prep
%setup -q -n %{tarballname}-%{version}

%build
./configure --prefix=%{_prefix}
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_prefix}/bin/gpp
%doc AUTHORS COPYING INSTALL NEWS README.md THANKS
%doc %{_prefix}/man/man1/gpp.1.gz



%changelog
* Mon Dec 20 2004 Tristan Miller <psychonaut@nothingisreal.com> - 
- Renamed package to genpp to avoid conflicts with obsolete GCC
  package of the same name.

* Fri Dec  3 2004 Tristan Miller <psychonaut@nothingisreal.com> - 
- Initial build.
