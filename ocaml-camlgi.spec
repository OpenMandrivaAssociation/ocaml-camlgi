%define up_name CamlGI
%define name	ocaml-camlgi
%define version	0.6
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	FastCGI and CGI library
Source: 	http://downloads.sourceforge.net/ocaml-cgi/%{up_name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/ocaml-cgi/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  ocaml-findlib
Conflicts:      %{name}-devel < 0.6-2mdv2008.0
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
CamlGI is a library to enable you to write CGI and FastCGI in OCaml. It is
written 100% in OCaml so should run on many platforms. The library supports
multiple simultaneous connections and request multiplexing while presenting an
easy to use interface.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
make install OCAMLFIND_DESTDIR="-destdir %{buildroot}/%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%dir %{_libdir}/ocaml/CamlGI
%{_libdir}/ocaml/CamlGI/*.cmi
%{_libdir}/ocaml/CamlGI/*.cma
%{_libdir}/ocaml/CamlGI/META

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/CamlGI/*
%exclude %{_libdir}/ocaml/CamlGI/*.cmi
%exclude %{_libdir}/ocaml/CamlGI/*.cma
%exclude %{_libdir}/ocaml/CamlGI/META


%changelog
* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-7mdv2010.0
+ Revision: 390539
- rebuild

  + Florent Monnier <blue_prawn@mandriva.org>
    - move non-devel files in main package
    - site-lib hierarchy doesn't exist anymore

* Tue Dec 09 2008 Pixel <pixel@mandriva.com> 0.6-6mdv2009.1
+ Revision: 312247
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2009.0
+ Revision: 254183
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-3mdv2008.1
+ Revision: 178363
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-2mdv2008.0
+ Revision: 78166
- add conflict to help upgrade
- fix summary
  drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage


* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2007.0
+ Revision: 122827

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2007.1
- first mdv release

