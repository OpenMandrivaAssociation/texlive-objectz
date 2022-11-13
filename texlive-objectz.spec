Name:		texlive-objectz
Version:	61719
Release:	1
Summary:	Macros for typesetting Object Z
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/objectz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will typeset both Z and Object-Z specifications; it
develops the original zed package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/objectz/oz.sty
%doc %{_texmfdistdir}/doc/latex/objectz/catalog
%doc %{_texmfdistdir}/doc/latex/objectz/makefile
%doc %{_texmfdistdir}/doc/latex/objectz/manifest
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.pdf
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.tex
%doc %{_texmfdistdir}/doc/latex/objectz/oztest.tex
%doc %{_texmfdistdir}/doc/latex/objectz/readme
#- source
%doc %{_texmfdistdir}/source/latex/objectz/oz.dtx
%doc %{_texmfdistdir}/source/latex/objectz/oz.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
