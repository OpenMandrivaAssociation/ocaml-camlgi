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
