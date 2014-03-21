%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define modname CamlGI

Summary:	FastCGI and CGI library
Name:		ocaml-camlgi
Version:	0.6
Release:	8
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://sourceforge.net/projects/ocaml-cgi/
Source0:	http://downloads.sourceforge.net/ocaml-cgi/%{modname}-%{version}.tar.bz2
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
CamlGI is a library to enable you to write CGI and FastCGI in OCaml. It is
written 100% in OCaml so should run on many platforms. The library supports
multiple simultaneous connections and request multiplexing while presenting an
easy to use interface.

%files
%doc LICENSE README
%dir %{_libdir}/ocaml/CamlGI
%{_libdir}/ocaml/CamlGI/*.cmi
%{_libdir}/ocaml/CamlGI/*.cma
%{_libdir}/ocaml/CamlGI/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/CamlGI/*
%exclude %{_libdir}/ocaml/CamlGI/*.cmi
%exclude %{_libdir}/ocaml/CamlGI/*.cma
%exclude %{_libdir}/ocaml/CamlGI/META

#----------------------------------------------------------------------------

%prep
%setup -q -n %{modname}-%{version}

%build
%make

%install
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
make install OCAMLFIND_DESTDIR="-destdir %{buildroot}/%{_libdir}/ocaml"

